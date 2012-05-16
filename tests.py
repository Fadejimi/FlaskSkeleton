import os
import main
import unittest
import tempfile
#import json

from pprint import pprint

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, main.app.config["DATABASE"] = tempfile.mkstemp()
        main.app.config["TESTING"] = True
        self.app = main.app.test_client()
        main.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(main.app.config["DATABASE"])

    def test_add_message(self):
        rv = self.app.get("/")
        assert "First Title" not in rv.data

        input = {}
        input["title"] = "First Title"
        input["message"] = "Message goes here." 

        rv = self.app.post("/addmessage", data=input, follow_redirects=True)
        assert "First Title" in rv.data

if __name__ == "__main__":
    unittest.main()
