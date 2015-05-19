class Mail(object):

    def __init__(self, _from="", _to="", _cc="", _bcc="", _subject="", _content="", _html_content="", _custom_headers="", _mime_raw=""):
        self.__from = _from
        self.__to = _to
        self.__cc = _cc
        self.__bcc = _bcc
        self.__subject = _subject
        self.__content = _content
        self.__html_content = _html_content
        self.__custom_headers = _custom_headers
        self.__mime_raw = _mime_raw

    def getFrom(self):
        return self.__from

    def getTo(self):
        return self.__to

    def getCc(self):
        return self.__cc

    def getBcc(self):
        return self.__bcc

    def getSubject(self):
        return self.__subject

    def getContent(self):
        return self.__content

    def getHtmlContent(self):
        return self.__html_content

    def getCustomHeaders(self):
        return self.__custom_headers

    def getMimeRaw(self):
        return self.__mime_raw

    def setFrom(self, _from):
        self.__from = _from

    def setTo(self, to):
        self.__to = to

    def setCc(self, cc):
        self.__cc = cc

    def setBcc(self, bcc):
        self.__bcc = bcc

    def setSubject(self, subject):
        self.__subject = subject

    def setContent(self, content):
        self.__content = content

    def setHtmlContent(self, html_content):
        self.__html_content = html_content

    def setCustomHeaders(self, custom_headers):
        self.__custom_headers = custom_headers

    def setMimeRaw(self, mime_raw):
        self.__mime_raw = mime_raw