class BabyMonitorCore(object):
    def _recording(self):
        while not self._exit.is_set():
            rec = self._recorder.record(self._config.babymonitor.record_time)
            self._recording_queue.put(rec)

    def _processing(self):
        import Queue

        while not self._exit.is_set():
            try:
                rec = self._recording_queue.get(timeout=0.2)
            except Queue.Empty:
                continue

            finger_print = self._analyzer.finger_print(rec)
            self._finger_print_queue.put(finger_print)

    def _detecting(self):
        import Queue

        while not self._exit.is_set():
            try:
                finger_print = self._finger_print_queue.get(timeout=0.2)
            except Queue.Empty:
                continue

            confidences = []
            match_found = False
            for reference in self._storage.get_finger_prints():
                if finger_print.compare(reference):
                    confidences.append(finger_print.compare_confidence(reference))
                    match_found = True

            if match_found:
                self._notify(max(confidences))

    def _notify(self, confidence):
        import datetime

        now = datetime.datetime.now()
        self._storage.add_occurence(now, confidence)

        if self._last_notification is None or (now - self._last_notification).total_seconds() > 300:
            self._last_notification = now

            self._detected.set()

            contents = "Piotr Placze!\nTime: {}\nConfidence: {:.2f} %".format(str(now),
                                                                              confidence)
            self._email.contents(contents)
            self._email.send(self._config.babymonitor.mail_list)

            print "###############################"
            print contents
