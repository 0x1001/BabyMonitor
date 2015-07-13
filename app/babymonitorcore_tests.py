import unittest


class TestBabyMonitorCore(unittest.TestCase):

    def setUp(self):
        import babymonitorcore
        import config
        import stubpyaudio

        stubpyaudio.init()

        cfg = config.Config("test_data/test_config.json.test")
        self.m = babymonitorcore.BabyMonitorCore(cfg)

    def tearDown(self):
        import stubpyaudio

        stubpyaudio.deinit()

    def test_babymonitorcore(self):
        self.m._recording()
        self.m._processing()
        self.m._detecting()
        self.m._notify([50, 24], ["test_test.wave", None])


if __name__ == "__main__":
    unittest.main()