def plot_day(day, file_path=None):
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import datetime

    occurences = _get_occurences()

    x = [day + datetime.timedelta(hours=i) for i in range(25)]
    y = [0] * 25

    for occur_time, occur_confidence in occurences:
        if day.strftime("%d%m%y") == occur_time.date().strftime("%d%m%y"):
            idx = int((occur_time - day).total_seconds() / (60 * 60))
            y[idx] += 1

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 12)
    plt.bar(x, y, color='g', align='center', width=0.02)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.axis([x[0] - datetime.timedelta(seconds=30 * 60), x[-1] + datetime.timedelta(seconds=30 * 60), 0, max(y) + max(y) * 0.1])
    plt.xticks(x)
    plt.ylabel('Occurences')
    plt.grid(True)
    fig.autofmt_xdate()

    if file_path is None:
        plt.show()
    else:
        plt.savefig(file_path)


def plot_months(file_path=None):
    import matplotlib.pyplot as plt
    import datetime
    import math
    import matplotlib.dates as mdates

    occurences = _get_occurences()

    first = occurences[0][0].date()
    last = datetime.datetime.now().date()

    days = int(math.ceil(((last - first).total_seconds() / (60 * 60 * 24)))) + 1

    x = [datetime.datetime.combine(first, datetime.time(hour=0, minute=0)) + datetime.timedelta(days=i) for i in range(days)]
    y = [0] * days
    for occur_time, occur_confidence in occurences:
        idx = int(math.ceil((occur_time.date() - first).total_seconds() / (60 * 60 * 24)))
        y[idx] += 1

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 12)
    plt.bar(x, y, color='r', align='center', width=0.5)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(x)
    plt.ylabel('Occurences')
    plt.grid(True)
    plt.axis([x[0] - datetime.timedelta(days=1), x[-1] + datetime.timedelta(days=1), 0, max(y) + max(y) * 0.1])
    fig.autofmt_xdate()

    if file_path is None:
        plt.show()
    else:
        plt.savefig(file_path)


def plot_confidence(file_path=None):
    import matplotlib.pyplot as plt

    occurences = _get_occurences()

    x = range(0, 101)
    y = [0] * 101
    for occur_time, occur_confidence in occurences:
        idx = int(occur_confidence)
        y[idx] += 1

    plt.bar(x, y, color='b', align='edge', width=1)
    plt.ylabel('Confidence')
    plt.grid(True)
    plt.axis([0, 101, 0, max(y) + max(y) * 0.1])

    if file_path is None:
        plt.show()
    else:
        plt.savefig(file_path)


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
    parser.add_argument("-o", "--output", type=str, help="Store graph instead of displaying it. Path to file.", dest="output")

    args = parser.parse_args()

    if args.day is not None:
        day = datetime.datetime.strptime(args.day, "%Y-%m-%d")
        plot_day(day, args.output)
    elif args.confidence:
        plot_confidence(args.output)
    else:
        plot_months(args.output)