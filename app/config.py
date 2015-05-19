class Config(object):

    def __init__(self, path=None, config=None):
        import json

        if path is not None:
            with open(path) as fp:
                config = json.load(fp)

        self._extract(config)

    def _extract(self, config):
        for key, value in config.items():
            if isinstance(value, dict):
                self.__dict__[key] = Config(config=value)
            else:
                self.__dict__[key] = value
