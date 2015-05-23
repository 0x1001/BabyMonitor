import babymonitorcore


class BabyMonitor(babymonitorcore.BabyMonitorCore):

    def __init__(self, *args):
        import multiprocessing

        super(BabyMonitor, self).__init__(*args)

        self._exit = multiprocessing.Event()
        self._recording_process = multiprocessing.Process(target=lambda: self._loop(self._recording))
        self._detecting_process = multiprocessing.Process(target=lambda: self._loop(self._detecting))

        self._processing_processes = []
        for i in range(2):
            self._processing_processes.append(multiprocessing.Process(target=lambda: self._loop(self._processing)))

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

    def _loop(self, func):
        while not self._exit.is_set():
            func()