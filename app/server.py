from twisted.internet import reactor, protocol


class AudioControl(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class Server(object):
    def start(self):
        import threading

        factory = protocol.ServerFactory()
        factory.protocol = AudioControl
        reactor.listenTCP(8000, factory)
        self._thread = threading.Thread(target=reactor.run, args=(False,))
        self._thread.start()

    def stop(self):
        reactor.callFromThread(reactor.stop)
        self._thread.join()
