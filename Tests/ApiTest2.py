import unittest
import requests

class MyTestCase(unittest.TestCase):

    def test_1(self):
        res = requests.get(url="http://127.0.0.1:5000/b7438d633dd9915c")
        self.assertEqual(res.status_code, 200)

    def test_2(self):
        res = requests.get(url="http://127.0.0.1:5000/b7438d633dd9915c")
        self.assertEqual("<class 'dict'>", str(type(eval(res.content))))

if __name__ == '__main__':
    unittest.main()
