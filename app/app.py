if __name__ == "__main__":
    import babymonitor
    import config

    cfg = config.Config("../config.json")

    b = babymonitor.BabyMonitor(cfg)
    b.start()
