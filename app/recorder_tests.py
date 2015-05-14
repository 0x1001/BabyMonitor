import unittest


class TestRecorder(unittest.TestCase):

    def test_record(self):
        import recorder

        r = recorder.Recorder()
        r.record(0.1)


if __name__ == "__main__":
    unittest.main()