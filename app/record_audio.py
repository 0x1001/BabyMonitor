def record(file_path, duration):
    import recorder

    r = recorder.Recorder()

    rec = r.record(duration)
    rec.save(file_path)


if __name__ == "__main__":
    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        type=str,
                        help="Path to new wave file",
                        dest="file",
                        default=str(datetime.datetime.now()) + ".wav")

    parser.add_argument("-t", "--time",
                        type=int,
                        help="Recording time",
                        dest="time",
                        default=2)

    args = parser.parse_args()

    record(args.file, args.time)