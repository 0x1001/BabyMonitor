import unittest


class TestStorage(unittest.TestCase):

    def test_storage(self):
        import storage
        import os

        storage.PATH = "/tmp/babymonitor.dumy.test"
        s = storage.Storage()

        data = [(1, 2), (1, 2)]

        s.add(data)
        data_read = s.get()

        os.unlink(storage.PATH)

        self.assertEqual(data_read, [data])


if __name__ == "__main__":
    unittest.main()