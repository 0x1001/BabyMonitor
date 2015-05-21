class BabyMonitor(object):

    def __init__(self):
        import config
        import multiprocessing
        import recorder
        import storage
        import analyzer
        import email

        self._config = config.Config("../config.json")
        self._recorder = recorder.Recorder()
        self._analyzer = analyzer.Analyzer()
        self._storage = storage.Storage()
        self._email = email.Email(self._config)
        self._last_notification = None

        self._exit = multiprocessing.Event()
        self._detected = multiprocessing.Event()
        self._recording_process = multiprocessing.Process(target=self._recording)
        self._detecting_process = multiprocessing.Process(target=self._detecting)
        self._recording_queue = multiprocessing.Queue()
        self._finger_print_queue = multiprocessing.Queue()

        self._processing_processes = []
        for i in range(2):
            self._processing_processes.append(multiprocessing.Process(target=self._processing))

    def start(self):
        self._recording_process.start()
        self._detecting_process.start()
        [p.start() for p in self._processing_processes]

        self._recording_process.join()
        self._detecting_process.join()
        [p.join() for p in self._processing_processes]

    def stop(self):
        self._exit.set()
        self._recorder.close()

    def _recording(self):
        while not self._exit.is_set():
            rec = self._recorder.record(self._config.babymonitor.record_time)
            self._recording_queue.put(rec)

    def _processing(self):
        import Queue

        while not self._exit.is_set():
            try:
                rec = self._recording_queue.get(timeout=0.2)
            except Queue.Empty:
                continue

            finger_print = self._analyzer.finger_print(rec)
            self._finger_print_queue.put(finger_print)

    def _detecting(self):
        import Queue

        while not self._exit.is_set():
            try:
                finger_print = self._finger_print_queue.get(timeout=0.2)
            except Queue.Empty:
                continue

            for reference in self._storage.get_finger_prints():
                if finger_print.compare(reference):
                    self._notify(finger_print.compare_confidence(reference))
                    break

    def _notify(self, confidence):
        import datetime

        now = datetime.datetime.now()

        if self._last_notification is None or (now - self._last_notification).total_seconds() > 300:
            self._last_notification = now

            self._detected.set()

            contents = "Piotr Placze!\nTime: {}\nConfidence: {:.2f} %".format(str(now),
                                                                              confidence)
            self._email.contents(contents)
            self._email.send(self._config.babymonitor.mail_list)

            self._storage.add_occurence(now, confidence)

            print "###############################"
            print contents
