class Analyzer(object):

    def finger_print(self, recording):
        import numpy as np
        import fingerprint

        if recording.data_format() == 2:
            data_type = np.int16
        else:
            raise Exception("Wrong data format!" + str(recording.format()))

        audio_data = np.fromstring(recording.data(), dtype=data_type)

        freq, amp = self._fft(audio_data)

        return fingerprint.FingerPrint(self._generate_print(freq, amp))

    def _fft(self, audio_data):
        from numpy import fft

        amp = fft.rfft(audio_data)
        freq = fft.fftfreq(audio_data.shape[-1])[:len(amp)]

        return freq, amp.real

    def _generate_print(self, freq, amp):
        data = zip(freq, amp)
        data.sort(key=lambda x: x[1], reverse=True)

        return data[:100]