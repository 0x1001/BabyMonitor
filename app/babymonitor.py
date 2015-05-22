import babymonitorcore


class BabyMonitor(babymonitorcore.BabyMonitorCore):
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

        self._recorder.close()

    def stop(self):
        self._exit.set()
        self._recording_process.terminate()
        self._detecting_process.terminate()
        [p.terminate() for p in self._processing_processes]
