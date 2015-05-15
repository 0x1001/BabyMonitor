class Recorder(object):
    _CHUNK = 512
    _RATE = 44100

    def __init__(self):
        import pyaudio

        self._audio = pyaudio.PyAudio()

        self._stream = self._audio.open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=self._RATE,
                                        input=True,
                                        frames_per_buffer=self._CHUNK)
        self._stream.stop_stream()

    def record(self, duration):
        self._stream.start_stream()

        frames = []
        for i in range(0, int(self._RATE / self._CHUNK * duration)):
            data = self._stream.read(self._CHUNK)
            frames.append(data)

        self._stream.stop_stream()

        return ''.join(frames)

    def close(self):
        self._stream.close()
        self._audio.terminate()

    def __del__(self):
        try:
            self.close()
        except:
            pass