import unittest


class TestRecorder(unittest.TestCase):
    def setUp(self):
        import stubpyaudio

        stubpyaudio.init()

    def tearDown(self):
        import stubpyaudio

        stubpyaudio.deinit()

    def test_record(self):
        import time
        import recorder

        r = recorder.Recorder()
        time.sleep(0.2)
        r.record(0.1)
        r.record(0.2)


if __name__ == "__main__":
    unittest.main()