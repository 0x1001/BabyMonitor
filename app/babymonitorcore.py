class BabyMonitorCore(object):

    def __init__(self, cfg):
        import multiprocessing
        import recorder
        import storage
        import analyzer
        import notifier

        self._config = cfg

        self._recorder = recorder.Recorder()
        self._analyzer = analyzer.Analyzer()
        self._notifier = notifier.Notifier(self._config)
        self._storage = storage.Storage(self._config)

        self._last_notification = None

        self._recording_queue = multiprocessing.Queue()
        self._finger_print_queue = multiprocessing.Queue()

    def _recording(self):
        rec = self._recorder.record(self._config.babymonitor.record_time)
        self._recording_queue.put(rec)

    def _processing(self):
        import Queue

        try:
            rec = self._recording_queue.get(timeout=0.2)
        except Queue.Empty:
            pass
        else:
            finger_print = self._analyzer.finger_print(rec)
            self._finger_print_queue.put(finger_print)

    def _detecting(self):
        import Queue

        try:
            finger_print = self._finger_print_queue.get(timeout=0.2)
        except Queue.Empty:
            pass
        else:
            confidences = []
            finger_print_names = []
            for reference in self._storage.get_finger_prints():
                if finger_print.compare(reference):
                    confidences.append(finger_print.compare_confidence(reference))
                    finger_print_names.append(reference.get_name())

            if confidences:
                self._notify(confidences, finger_print_names)

    def _notify(self, confidences, finger_print_names):
        import datetime

        now = datetime.datetime.now()
        self._storage.add_occurence(now, max(confidences))
        contents = self._format_occurences(now, confidences, finger_print_names)
        self._print_occurences(contents)

        if self._last_notification is None or (now - self._last_notification).total_seconds() > 300:
            self._last_notification = now
            self._notifier.notify(contents)

    def _format_occurences(self, now, confidences, finger_print_names):
        contents = "Piotr Placze!\nTime: {}\n\n".format(str(now))

        for i in range(len(confidences)):
            contents += "Confidence: {:.2f} % Finger print name: {:s}\n".format(confidences[i], finger_print_names[i])

        return contents

    def _print_occurences(self, contents):
        print "###############################"
        print contents
