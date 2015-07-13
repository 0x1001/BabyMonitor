def add_finger_print(file_path):
    import wave
    import analyzer
    import storage
    import recording
    import config
    import os

    a = analyzer.Analyzer()
    s = storage.Storage(config.Config("../config.json"))

    waveFile = wave.open(file_path)
    waveData = waveFile.readframes(waveFile.getnframes())

    rec = recording.Recording(waveData, waveFile.getframerate(), waveFile.getsampwidth(), waveFile.getnchannels())

    finger_print = a.finger_print(rec)
    finger_print.set_name(os.path.basename(file_path))

    s.add_finger_print(finger_print)

if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="Path to wave file", dest="file")
    parser.add_argument("-d", "--dir", type=str, help="Path to folder with wave files", dest="dir")

    args = parser.parse_args()

    if args.dir is not None:
        waves = [os.path.join(args.dir, file_name) for file_name in os.listdir(args.dir) if file_name.endswith(".wav")]
    else:
        waves = [args.file]

    for wave in waves:
        print "Processing: " + wave
        add_finger_print(wave)