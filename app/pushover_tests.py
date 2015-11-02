import unittest


class TestPushover(unittest.TestCase):
    def test_pushover(self):
        import pushover
        import config

        contents = "test test"
        cfg = config.Config("test_data/test_config.json.test")

        n = pushover.Pushover(cfg)
        n.send(contents)


if __name__ == "__main__":
    unittest.main()