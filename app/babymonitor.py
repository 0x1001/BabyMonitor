RECORD_TIME = 2


class BabyMonitor(object):

    def __init__(self):
        import recorder
        import storage
        import analyzer

        self._recorder = recorder.Recorder()
        self._analyzer = analyzer.Analyzer()
        self._storage = storage.Storage()

    def start(self):
        import time

        while True:
            data = self._recorder.record(RECORD_TIME)
            finger_print = self._analyzer.finger_print(data)

            for reference in self._storage.get():
                if finger_print.compare(reference):
                    print "Detected!"

            time.sleep(0.2)
