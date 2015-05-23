class StubStream(object):

    def start_stream(self):
        pass

    def stop_stream(self):
        pass

    def read(self, *args):
        return "dummy_data"

    def close(self):
        pass


class StubPyAudio(object):
    def get_sample_size(self, *args):
        return 2

    def open(self, *args, **kargs):
        return StubStream()


def init():
    import pyaudio

    pyaudio.PyAudio = StubPyAudio


def deinit():
    import pyaudio

    reload(pyaudio)