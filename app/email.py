class Email(object):
    def __init__(self, config):
        from turbosmtp import mail
        from turbosmtp import turbosmtp

        self._server = turbosmtp.TurboSMTP(config.email.username, config.email.password)

        self._mail = mail.Mail()
        self._mail.setFrom("babymonitor@venus")
        self._mail.setSubject("Piotr placze!")

    def contents(self, contents):
        self._mail.setContent(contents)

    def send(self, addresses):
        for address in addresses:
            self._mail.setTo(address)
            self._server.send(self._mail)