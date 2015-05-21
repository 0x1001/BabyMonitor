def add_finger_print(file_path):
    import wave
    import analyzer
    import storage
    import recording

    a = analyzer.Analyzer()
    s = storage.Storage()

    waveFile = wave.open(file_path)
    waveData = waveFile.readframes(waveFile.getnframes())

    rec = recording.Recording(waveData, waveFile.getframerate(), waveFile.getsampwidth(), waveFile.getnchannels())

    finger_print = a.finger_print(rec)

    s.add_finger_print(finger_print)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="Path to wave file", dest="file")
    parser.add_argument("-l", "--list", type=str, help="Path to wave file list", dest="list")

    args = parser.parse_args()

    if args.list is not None:
        with open(args.list) as fp:
            waves = fp.readlines()

        waves = [wave.strip() for wave in waves]

    else:
        waves = [args.file]

    for wave in waves:
        print "Processing: " + wave
        add_finger_print(wave)