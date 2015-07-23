import unittest


class TestEmail(unittest.TestCase):

    def test_email(self):
        import emailmessage
        import config

        class DummyServer(object):
            def send(self, *args):
                pass

        cfg = config.Config("../config.json_example")
        e = emailmessage.EmailMessage(cfg)
        e._server = DummyServer()
        e.send(["dummy@dummy.eu"])

    @unittest.skip("Sending real email")
    def test_real_email(self):
        import emailmessage
        import config

        cfg = config.Config("../config.json")
        e = emailmessage.EmailMessage(cfg)
        e.contents("Test Test")
        e.send(["damian.nowok@gmail.com"])

    @unittest.skip("Sending real email with attachment")
    def test_real_email_with_attachment(self):
        import emailmessage
        import config

        cfg = config.Config("../config.json")
        e = emailmessage.EmailMessage(cfg)
        e.contents("Test 2. Test 2")
        e.attach(__file__)
        e.send(["damian.nowok@gmail.com"])

if __name__ == "__main__":
    unittest.main()