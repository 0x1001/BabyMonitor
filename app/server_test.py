import unittest


class TestServer(unittest.TestCase):

    def test_server(self):
        import server

        s = server.Server()
        s.start()
        s.stop()

if __name__ == "__main__":
    unittest.main()