class BabyMonitor(object):

    def __init__(self):
        import config
        import threading
        import recorder
        import storage
        import analyzer

        self._config = config.Config("../config.json")
        self._recorder = recorder.Recorder()
        self._analyzer = analyzer.Analyzer()
        self._storage = storage.Storage()

        self._exit = threading.Event()
        self._detected = threading.Event()

    def start(self):
        import email
        import datetime

        while not self._exit.wait(0.2):
            rec = self._recorder.record(int(self._config.babymonitor.record_time))
            finger_print = self._analyzer.finger_print(rec)

            for reference in self._storage.get():
                if finger_print.compare(reference):
                    self._detected.set()
                    e = email.Email(self._config)
                    contents = "Piotr Placze!\nTime: {}\nConfidence: {:.2f} %".format(str(datetime.datetime.now()),
                                                                                      finger_print.compare_confidence(reference))
                    e.contents(contents)
                    e.send(self._config.babymonitor.mail_list)
                    print "###############################"
                    print contents
                    break

    def stop(self):
        self._exit.set()
        self._recorder.close()