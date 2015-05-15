PATH = "../finger_prints.pckl"


class Storage(object):

    def __init__(self):
        import os
        import pickle

        if os.path.isfile(PATH):
            with open(PATH, 'rb') as fp:
                self._db = pickle.load(fp)
        else:
            self._db = []

    def add(self, finger_print):
        self._db.append(finger_print)
        self._save()

    def get(self):
        return self._db

    def _save(self):
        import pickle

        with open(PATH, 'wb') as fp:
            pickle.dump(self._db, fp)
