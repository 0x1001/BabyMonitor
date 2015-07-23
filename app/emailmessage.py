class EmailMessage(object):
    def __init__(self, config):
        import turbosmtp
        from email.mime.multipart import MIMEMultipart

        self._server = turbosmtp.TurboSMTP(config.email.username, config.email.password)

        self._msg = MIMEMultipart()
        self._msg["From"] = "babymonitor@venus.raspberry"
        self._msg["Subject"] = "Baby Monitor"

    def contents(self, contents):
        from email.mime.text import MIMEText

        text = MIMEText(contents, "plain")
        self._msg.attach(text)

    def attach(self, file_path):
        import os
        from email.mime.base import MIMEBase

        att = MIMEBase("application", "octet-stream")
        with open(file_path, "rb") as fp:
            att.set_payload(fp.read())

        att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))

        self._msg.attach(att)

    def send(self, addresses):
        import turbosmtp

        for address in addresses:
            self._msg["To"] = address

            try:
                self._server.send(self._msg)
            except turbosmtp.TurboSMTPException as error:
                print "Cannot send email: " + str(error)