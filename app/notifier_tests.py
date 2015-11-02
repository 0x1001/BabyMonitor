import unittest


class TestNotifier(unittest.TestCase):
    def test_notify(self):
        import notifier
        import config

        contents = "test test"
        cfg = config.Config("test_data/test_config.json.test")
        n = notifier.Notifier(cfg)
        n.notify(contents)


if __name__ == "__main__":
    unittest.main()
