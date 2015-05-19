import unittest


class TestConfig(unittest.TestCase):
    def test_config(self):
        import config

        c = config.Config("../config.json_example")
        self.assertEqual(c.email.username, "example_username")
        self.assertEqual(c.email.password, "example_password")


if __name__ == "__main__":
    unittest.main()