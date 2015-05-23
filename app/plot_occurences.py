def plot_day(day):
    import matplotlib.pyplot as plt
    import datetime

    occurences = _get_occurences()

    x = range(24)
    y = [0] * 24

    midnight = datetime.datetime.combine(day, datetime.time(hour=0, minute=0))

    for occur_time, occur_confidence in occurences:
        if day.strftime("%d%m%y") == occur_time.date().strftime("%d%m%y"):
            idx = int((occur_time - midnight).total_seconds() / (60 * 60))
            y[idx] += 1

    plt.bar(x, y, color='g', align='edge', width=1)
    plt.ylabel('Occurences')
    plt.grid(True)
    plt.axis([0, 24, 0, max(y) + max(y) * 0.1])
    plt.show()


def plot_all():
    import matplotlib.pyplot as plt
    import datetime
    import math

    occurences = _get_occurences()

    first = occurences[0][0].date()
    last = datetime.datetime.now().date()

    days = int(math.ceil(((last - first).total_seconds() / (60 * 60 * 24)))) + 1

    x = range(days)
    y = [0] * days
    for occur_time, occur_confidence in occurences:
        idx = int(math.ceil((occur_time.date() - first).total_seconds() / (60 * 60 * 24)))
        y[idx] += 1

    plt.bar(x, y, color='r', align='edge', width=1)
    plt.ylabel('Occurences')
    plt.grid(True)
    plt.axis([0, days, 0, max(y) + max(y) * 0.1])
    plt.show()


def plot_confidence():
    import matplotlib.pyplot as plt

    occurences = _get_occurences()

    x = range(0, 100)
    y = [0] * 100
    for occur_time, occur_confidence in occurences:
        idx = int(occur_confidence)
        y[idx] += 1

    plt.bar(x, y, color='b', align='edge', width=1)
    plt.ylabel('Confidence')
    plt.grid(True)
    plt.axis([0, 100, 0, max(y) + max(y) * 0.1])
    plt.show()


def _get_occurences():
    import storage
    import config

    s = storage.Storage(config.Config("../config.json"))
    return s.get_occurences()


if __name__ == "__main__":
    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=str, help="Plot daily occurences. Date format: 2015-05-22", dest="day")
    parser.add_argument("-c", "--confidence", action='store_true', help="Plot confidence ranges", dest="confidence")

    args = parser.parse_args()

    if args.day is not None:
        day = datetime.datetime.strptime(args.day, "%Y-%m-%d")
        plot_day(day)
    elif args.confidence:
        plot_confidence()
    else:
        plot_all()