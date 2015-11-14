import unittest


class TestPushover(unittest.TestCase):
    def setUp(self):
        import config

        self.cfg = config.Config("test_data/test_config.json.test")

        self.contents = "test test"

    def test_pushover(self):
        import pushover

        n = pushover.Pushover(self.cfg)
        n.send(self.contents)

    def test_pushover_exception(self):
        import pushover
        import httplib
        import socket

        def mock_request(*args):
            raise socket.gaierror()

        httplib.HTTPSConnection.request = mock_request

        n = pushover.Pushover(self.cfg)
        n.send(self.contents)


if __name__ == "__main__":
    unittest.main()