class Recorder(object):
    _CHUNK = 1024
    _RATE = 44100
    _CHANNELS = 1

    def __init__(self):
        import pyaudio

        self._audio = pyaudio.PyAudio()

        self._FORMAT = self._audio.get_sample_size(pyaudio.paInt16)

        self._stream = self._audio.open(format=pyaudio.paInt16,
                                        channels=self._CHANNELS,
                                        rate=self._RATE,
                                        input=True,
                                        frames_per_buffer=self._CHUNK / 2,
                                        start=False)

    def record(self, duration):
        import datetime

        self._stream.start_stream()

        while True:
            try:
                rec = self._record(duration)
            except Exception as error:
                print str(datetime.datetime.now()) + " - Overflow happend! " + str(error)
            else:
                break

        self._stream.stop_stream()

        return rec

    def _record(self, duration):
        import recording

        frames = []
        for i in range(0, int(self._RATE / self._CHUNK * duration)):
            try:
                data = self._stream.read(self._CHUNK)
            except IOError:
                raise Exception(str(i))
            frames.append(data)

        return recording.Recording(b''.join(frames), self._RATE, self._FORMAT, self._CHANNELS)

    def close(self):
        self._stream.close()
        self._audio.terminate()

    def __del__(self):
        try:
            self.close()
        except:
            pass