class FingerPrint(object):

    def __init__(self, finger_print):
        self._data = finger_print

    def compare(self, finger_print, tolerance, threshold):
        data = finger_print.data()

        if len(self._data) > len(data):
            return False

        hits = 0
        for i in range(len(self._data)):
            first_freq, first_amp = self._data[i]
            second_freq, second_amp = data[i]

            if first_freq - tolerance <= second_freq and second_freq <= first_freq + tolerance:
                hits += 1

        if 100 * hits / len(self._data) > threshold:
            return True
        else:
            return False

    def data(self):
        return self._data