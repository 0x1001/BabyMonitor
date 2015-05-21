import unittest
import email
import storage


class TestBabyMonitor(unittest.TestCase):
    class StubRecorder(object):
        def __init__(self, file_name):
            self._file_name = file_name

        def record(self, _):
            import wave
            import recording

            waveFile = wave.open(self._file_name)

            return recording.Recording(waveFile.readframes(waveFile.getnframes()),
                                        waveFile.getframerate(),
                                        waveFile.getsampwidth(),
                                        waveFile.getnchannels())

        def close(self):
            pass

    class StubStorage(storage.Storage):
        def add_occurence(self, *args):
            pass

    class StubEmail(email.Email):
        def send(self, *args):
            pass

    @unittest.skip("Full blown test")
    def test_babymonitor(self):
        self.babymonitor("test_data/__rec_20150426-1033.wav", False)
        self.babymonitor("test_data/2015-05-17 22:25:59.451634.wav", True)

    def babymonitor(self, file_name, outcome):
        import babymonitor
        import threading
        import time

        b = babymonitor.BabyMonitor()
        b._recorder = self.StubRecorder(file_name)

        t = threading.Thread(target=b.start)
        t.start()

        time.sleep(5)
        b.stop()

        t.join()

        self.assertEqual(b._detected.is_set(), outcome)

if __name__ == "__main__":
    unittest.main()