class Recording(object):

    def __init__(self, data, rate, data_format, channels):
        self._data = data
        self._format = data_format
        self._rate = rate
        self._channels = channels

    def save(self, file_path):
        import wave

        fp = wave.open(file_path, 'wb')
        fp.setnchannels(self._channels)
        fp.setsampwidth(self._format)
        fp.setframerate(self._rate)
        fp.writeframes(self._data)
        fp.close()

    def data(self):
        return self._data

    def data_format(self):
        return self._format
