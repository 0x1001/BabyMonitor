TOLERANCE = 0.002
THRESHOLD = 25


class FingerPrint(object):

    def __init__(self, finger_print):
        self._data = finger_print
        self._name = None

    def compare(self, finger_print):
        if self.compare_confidence(finger_print) > THRESHOLD:
            return True
        else:
            return False

    def compare_confidence(self, finger_print):
        data = finger_print.data()

        if len(self._data) > len(data):
            return False

        hits = 0
        for i in range(len(self._data)):
            first_freq, first_amp = self._data[i]
            second_freq, second_amp = data[i]

            if first_freq - TOLERANCE <= second_freq and second_freq <= first_freq + TOLERANCE:
                hits += 1

        return 100 * hits / len(self._data)

    def data(self):
        return self._data

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name