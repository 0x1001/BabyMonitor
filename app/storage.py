FINGER_PRINT_DB = "../finger_prints.pckl"
OCCURENCE_DB = "../occurences.pckl"


class Storage(object):

    def __init__(self):
        self._finger_print_db = self._load(FINGER_PRINT_DB)
        self._occurence_db = self._load(OCCURENCE_DB)

    def add_finger_print(self, finger_print):
        self._finger_print_db.append(finger_print)
        self._save(FINGER_PRINT_DB, self._finger_print_db)

    def get_finger_prints(self):
        return self._finger_print_db

    def add_occurence(self, time, confidence):
        self._occurence_db.append((time, confidence))
        self._save(OCCURENCE_DB, self._occurence_db)

    def get_occurences(self):
        return self._occurence_db

    def _load(self, file_path):
        import os
        import pickle

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as fp:
                return pickle.load(fp)
        else:
            return []

    def _save(self, file_path, db):
        import pickle

        with open(file_path, 'wb') as fp:
            pickle.dump(db, fp)
