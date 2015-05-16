TOLERANCE = 0.002
THRESHOLD = 10


class FingerPrint(object):

    def __init__(self, finger_print):
        self._data = finger_print

    def compare(self, finger_print):
        data = finger_print.data()

        if len(self._data) > len(data):
            return False

        hits = 0
        for i in range(len(self._data)):
            first_freq, first_amp = self._data[i]
            second_freq, second_amp = data[i]

            if first_freq - TOLERANCE <= second_freq and second_freq <= first_freq + TOLERANCE:
                hits += 1

        if 100 * hits / len(self._data) > THRESHOLD:
            return True
        else:
            return False

    def data(self):
        return self._data