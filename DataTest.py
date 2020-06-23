import unittest
from DataHandling import Data


class Test(unittest.TestCase):

    def test_main(self):
        d = Data()
        d.update({"testdata_1":123})
        d.update({"testdata_2":456})
        self.assertDictEqual(d.json, {1: {"testdata_1": 123}, 2: {"testdata_2": 456}})

if __name__ == '__main__':
    unittest.main()
