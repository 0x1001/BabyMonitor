import unittest


class TestAnalyzer(unittest.TestCase):

    def test_finger_print(self):
        import analyzer

        a = analyzer.Analyzer()
        a.finger_print("aaaaaaaaaa")


if __name__ == "__main__":
    unittest.main()