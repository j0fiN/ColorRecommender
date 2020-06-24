import unittest
from ColorPickerModel import ML_Model


class TestCase(unittest.TestCase):

    def test_1(self):
        m = ML_Model()
        self.assertEqual(200, m.res.status_code)

    def test_2(self):
        m = ML_Model()
        print(m.data)
        self.assertEqual(len(m.predictor(0, 0, 0)), 1)

    def test_3(self):
        m = ML_Model()
        self.assertEqual(m.preprocess(), None)

    def test_4(self):
        m = ML_Model()
        m.preprocess()
        self.assertIsNotNone(m.train())


if __name__ == '__main__':
    unittest.main()
