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
        import numpy as np

        amp = fft.fft(audio_data)
        amp = amp.real
        freq = fft.fftfreq(audio_data.shape[-1])

        to_delete = []
        for i in range(len(amp)):
            if freq[i] < 0 or amp[i] < 0:
                to_delete.append(i)

        amp = np.delete(amp, to_delete)
        freq = np.delete(freq, to_delete)

        return freq, amp

    def _generate_print(self, freq, amp):
        data = zip(freq, amp)
        data.sort(key=lambda x: x[1], reverse=True)

        return data[:100]