class Notifier(object):
    def __init__(self, config):
        import pushover

        self._config = config
        self._pushover = pushover.Pushover(self._config)

    def notify(self, contents):
        self._send_email(contents)
        self._send_notification(contents)

    def _send_email(self, contents):
        import emailmessage

        email = emailmessage.EmailMessage(self._config)
        email.contents(contents)
        email.send(self._config.babymonitor.mail_list)

    def _send_notification(self, contents):
        self._pushover.send(contents)
