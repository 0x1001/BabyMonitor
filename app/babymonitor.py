RECORD_TIME = 2


class BabyMonitor(object):

    def __init__(self):
        import threading
        import recorder
        import storage
        import analyzer

        self._recorder = recorder.Recorder()
        self._analyzer = analyzer.Analyzer()
        self._storage = storage.Storage()

        self._exit = threading.Event()
        self._detected = threading.Event()

    def start(self):
        while not self._exit.wait(0.2):
            data = self._recorder.record(RECORD_TIME)
            finger_print = self._analyzer.finger_print(data)

            for reference in self._storage.get():
                if finger_print.compare(reference):
                    self._detected.set()
                    import datetime
                    print str(datetime.datetime.now()) + " - Detected!"

    def stop(self):
        self._exit.set()
        self._recorder.close()