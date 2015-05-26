class Email(object):
    def __init__(self, config):
        from turbosmtp import mail
        from turbosmtp import turbosmtp

        self._server = turbosmtp.TurboSMTP(config.email.username, config.email.password)

        self._mail = mail.Mail()
        self._mail.setFrom("babymonitor@venus.raspberry")
        self._mail.setSubject("Baby Monitor")

    def contents(self, contents):
        self._mail.setContent(contents)

    def attach(self, file_path):
        self._mail.setAttachment(file_path)

    def send(self, addresses):
        from turbosmtp import turbosmtp
        for address in addresses:
            self._mail.setTo(address)
            try:
                self._server.send(self._mail)
            except turbosmtp.TurboSMTPException as error:
                print "Cannot send email: " + str(error)