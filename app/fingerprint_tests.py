import unittest


class TestFingerPrint(unittest.TestCase):

    def test_compare(self):
        import fingerprint

        f1 = fingerprint.FingerPrint([(1, 2), (2, 3)])
        f2 = fingerprint.FingerPrint([(1, 2), (2, 3)])

        self.assertTrue(f1.compare(f2, 0.01, 50))

if __name__ == "__main__":
    unittest.main()