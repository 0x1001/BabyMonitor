import unittest


class TestAnalyzer(unittest.TestCase):

    def test_finger_print(self):
        import analyzer
        import recording

        rec = recording.Recording("abcdefghijklamneopersssaaa", 44100, 2, 1)

        a = analyzer.Analyzer()
        finger_print = a.finger_print(rec)._data

        ref = [(0.0, 350286.0), (0.23076923076923078, 3429.927826131363), (0.38461538461538464, 1469.368146510493), (0.30769230769230771, 1348.5880395096622)]

        for i in range(len(ref)):
            self.assertAlmostEqual(finger_print[i][0], ref[i][0], places=3)
            self.assertAlmostEqual(finger_print[i][1], ref[i][1], places=3)

if __name__ == "__main__":
    unittest.main()