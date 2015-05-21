import unittest


class TestStorage(unittest.TestCase):
    TEMP_DB = "/tmp/babymonitor.dumy.test"

    def setUp(self):
        import os

        if os.path.isfile(self.TEMP_DB):
            os.unlink(self.TEMP_DB)

    def test_storage_finger_prints(self):
        import storage
        import os

        storage.FINGER_PRINT_DB = self.TEMP_DB
        s = storage.Storage()

        data = [(1, 2), (1, 2)]

        s.add_finger_print(data)
        data_read = s.get_finger_prints()

        os.unlink(self.TEMP_DB)

        self.assertEqual(data_read, [data])

    def test_storage_occurences(self):
        import storage
        import os
        import datetime

        time = datetime.datetime.now()
        confidence = 50

        storage.OCCURENCE_DB = self.TEMP_DB
        s = storage.Storage()
        s.add_occurence(time, confidence)
        s.get_occurences()

        os.unlink(self.TEMP_DB)

if __name__ == "__main__":
    unittest.main()