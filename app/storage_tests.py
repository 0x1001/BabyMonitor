import unittest


class TestStorage(unittest.TestCase):
    TEMP_DB = "/tmp/babymonitor.dumy.test"

    def tearDown(self):
        self._clean()

    def setUp(self):
        import storage
        import config

        cfg = config.Config("test_data/test_config.json")
        self.s = storage.Storage(cfg)
        self._clean()

    def test_storage_finger_prints(self):
        data = [(1, 2), (1, 2)]

        self.s.add_finger_print(data)
        data_read = self.s.get_finger_prints()

        self.assertEqual(data_read, [data])

    def test_storage_occurences(self):
        import datetime

        time = datetime.datetime.now()
        confidence = 50

        self.s.add_occurence(time, confidence)
        self.s.get_occurences()

    def _clean(self):
        import os
        import config

        cfg = config.Config("test_data/test_config.json")

        if os.path.isfile(cfg.storage.finger_print_db):
            os.unlink(cfg.storage.finger_print_db)

        if os.path.isfile(cfg.storage.occurence_db):
            os.unlink(cfg.storage.occurence_db)

if __name__ == "__main__":
    unittest.main()