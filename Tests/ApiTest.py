import requests
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        res = requests.post(url="http://127.0.0.1:5000/api", json={"key": 3, "note": "C"})
        self.assertEqual(res.status_code, 200)

    def test_2(self):
        res = requests.post(url="http://127.0.0.1:5000/api", json={"key": 3, "note": "C"})
        self.assertIsNotNone(res.content)

if __name__ =="__main__":
    unittest.main()

