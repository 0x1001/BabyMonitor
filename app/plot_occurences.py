def plot_day(day):
    import matplotlib.pyplot as plt
    import datetime

    occurences = _get_occurences()

    x = []
    y = []
    for hour in range(24):
        time = datetime.time(hour=hour, minute=0)
        day_time = datetime.datetime.combine(day, time)
        x.append(hour)
        y.append(0)

        for occur_time, occur_confidence in occurences:
            if day_time <= occur_time and occur_time <= day_time + datetime.timedelta(hours=1):
                y[hour] += 1

    plt.bar(x, y, color='g', align='center', width=0.5)
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
        idx = int(math.ceil((last - occur_time.date()).total_seconds() / (60 * 60 * 24)))
        y[idx] += 1

    plt.bar(x, y, color='r', align='center', width=0.5)
    plt.ylabel('Occurences')
    plt.grid(True)
    plt.axis([0, days, 0, max(y) + max(y) * 0.1])
    plt.show()


def _get_occurences():
    import storage

    s = storage.Storage()
    return s.get_occurences()


if __name__ == "__main__":
    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=str, help="Plot daily occurences. Date format: 2015-05-22", dest="day")

    args = parser.parse_args()

    if args.day is not None:
        day = datetime.datetime.strptime(args.day, "%Y-%m-%d")
        plot_day(day)
    else:
        plot_all()