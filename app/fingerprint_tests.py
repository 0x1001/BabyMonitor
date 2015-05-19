import unittest


class TestFingerPrint(unittest.TestCase):

    def test_compare_true(self):
        import fingerprint

        f1 = fingerprint.FingerPrint([(1, 2), (2, 3)])
        f2 = fingerprint.FingerPrint([(1, 2), (2, 3)])

        self.assertTrue(f1.compare(f2))

    def test_compare_false(self):
        import fingerprint

        f1 = fingerprint.FingerPrint([(1, 2), (2, 3)])
        f2 = fingerprint.FingerPrint([(100, 200), (200, 300)])

        self.assertFalse(f1.compare(f2))

if __name__ == "__main__":
    unittest.main()