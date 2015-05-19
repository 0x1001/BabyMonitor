class TurboSMTPException(Exception):
    pass


class TurboSMTP(object):
    SERVER_URL = "https://api.turbo-smtp.com/api/mail/send"

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def send(self, mail):
        import urllib
        import urllib2

        dataToSend = {
                       'authuser': self._username,
                       'authpass': self._password,
                       'from': mail.getFrom(),
                       'to': mail.getTo(),
                       'cc': mail.getCc(),
                       'bcc': mail.getBcc(),
                       'subject': mail.getSubject(),
                       'content': mail.getContent(),
                       'html_content': mail.getHtmlContent(),
                       'custom_headers': mail.getCustomHeaders(),
                       'mime_raw': mail.getMimeRaw()
                     }

        try:
            encodedDataToSend = urllib.urlencode(dataToSend)
            req = urllib2.Request(self.SERVER_URL, encodedDataToSend)
            response = urllib2.urlopen(req)
            return response.read()
        except urllib2.HTTPError as error:
            raise TurboSMTPException(error)
