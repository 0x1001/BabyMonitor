class Pushover(object):
    def __init__(self, config):
        try:
            self._token = config.pushover.token
            self._user = config.pushover.user
        except AttributeError:
            self._disabled = True
        else:
            self._disabled = False

    def send(self, contents):
        import httplib
        import socket

        if self._disabled:
            return

        try:
            response = self._send_notification(contents)
        except (httplib.HTTPException, socket.error) as error:
            print "Cannot send notification via Pushover. Error: " + str(error)
        else:
            self._analyze_server_response(response)

    def _send_notification(self, contents):
        import urllib
        import httplib

        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST",
                     "/1/messages.json",
                     urllib.urlencode({"token": self._token,
                                       "user": self._user,
                                       "message": contents}),
                     {"Content-type": "application/x-www-form-urlencoded"})

        return conn.getresponse()

    def _analyze_server_response(self, response):
        import json

        resp_contents = response.read()
        server_msg = json.loads(resp_contents)
        if server_msg["status"] == 0:
            print "Error during sending Pushover notification: " + ", ".join(server_msg["errors"])
