import unittest


class TestRecording(unittest.TestCase):

    def test_recording(self):
        import recording
        import os

        file_path = "/tmp/recording_test_dummy.wav"

        data = 'ffffff'
        rate = 44100
        data_format = 2
        channels = 1

        r = recording.Recording(data, rate, data_format, channels)
        r.save(file_path)

        os.unlink(file_path)

if __name__ == "__main__":
    unittest.main()