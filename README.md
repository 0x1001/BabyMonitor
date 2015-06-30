# BabyMonitor

Raspberry PI Baby Monitor.

  - Detects baby cry
  - Notifies via email about baby cry
  - Plots graphs with baby cry statistics

## Version

1.0.0

## List of third party libraries
- [NumPy]
- [Matplotlib]
- [pyaudio]

## Installation

You need to get this repo to your Raspberry Pi by doing:
```sh
$ git clone https://github.com/0x1001/BabyMonitor.git
```
Then run installer:
```sh
$ cd BabyMonitor
$ ./install.sh
```

## Starting and Stopping

```sh
$ ./babymonitor.sh start
```

```sh
$ ./babymonitor.sh stop
```

## Change log

- 1.0.0
    - Initial version
    - Baby cry detection
    - Email notification
    - Statistics

## Want to contribute?

Anyone is welcome to contribute to this project :).
Just contact me on Github.

## License

GNU GENERAL PUBLIC LICENSE

[NumPy]:http://www.numpy.org/
[Matplotlib]:http://matplotlib.org/
[pyaudio]:https://people.csail.mit.edu/hubert/pyaudio/
