class Mail(object):

    def __init__(self, _from="", _to="", _cc="", _bcc="", _subject=""):
        import uuid

        self._boundry = uuid.uuid4().hex

        self._from = _from
        self._to = _to
        self._cc = _cc
        self._bcc = _bcc
        self._subject = _subject
        self._mime_raw = "Content-Type: multipart/mixed; boundary=" + self._boundry + "\n\n"

    def getFrom(self):
        return self._from

    def getTo(self):
        return self._to

    def getCc(self):
        return self._cc

    def getBcc(self):
        return self._bcc

    def getSubject(self):
        return self._subject

    def getMimeRaw(self):
        return self._mime_raw + "\n--" + self._boundry + "--\n"

    def getContent(self):
        return ""

    def getCustomHeaders(self):
        return ""

    def getHtmlContent(self):
        return ""

    def setFrom(self, _from):
        self._from = _from

    def setTo(self, to):
        self._to = to

    def setCc(self, cc):
        self._cc = cc

    def setBcc(self, bcc):
        self._bcc = bcc

    def setSubject(self, subject):
        self._subject = subject

    def setContent(self, content):
        self._mime_raw += "--" + self._boundry + "\n"
        self._mime_raw += "Content-Type: text/plain; charset=UTF-8\n"
        self._mime_raw += "\n"
        self._mime_raw += content
        self._mime_raw += "\n"

    def setAttachment(self, file_path):
        import os

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        self._mime_raw += "--" + self._boundry + "\n"
        self._mime_raw += "Content-Type: text/plain; name=\"" + file_name + "\"\n"
        self._mime_raw += "Content-Description: " + file_name + "\n"
        self._mime_raw += "Content-Disposition: attachment; filename=\"" + file_name + "\"; size=" + str(file_size) + "\n"
        self._mime_raw += "Content-Transfer-Encoding: base64\n"
        self._mime_raw += "\n"

        with open(file_path, "rb") as fp:
            contents = fp.read().encode("base64")

        self._mime_raw += contents
        self._mime_raw += "\n"
