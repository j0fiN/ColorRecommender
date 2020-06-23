import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import requests

test_data = {'1': {'b': 92, 'g': 164, 'r': 238, 'rate': 1},
             '2': {'b': 123, 'g': 27, 'r': 176, 'rate': 1},
             '3': {'b': 228, 'g': 217, 'r': 208, 'rate': 1},
             '4': {'b': 41, 'g': 242, 'r': 208, 'rate': 3},
             '5': {'b': 196, 'g': 100, 'r': 17, 'rate': 1},
             '6': {'b': 237, 'g': 111, 'r': 248, 'rate': 3},
             '7': {'b': 208, 'g': 229, 'r': 29, 'rate': 3},
             '8': {'b': 6, 'g': 102, 'r': 144, 'rate': 2},
             '9': {'b': 232, 'g': 16, 'r': 111, 'rate': 3},
             '10': {'b': 82, 'g': 9, 'r': 57, 'rate': 1},
             '11': {'b': 162, 'g': 223, 'r': 32, 'rate': 1},
             '12': {'b': 0, 'g': 141, 'r': 210, 'rate': 1},
             '13': {'b': 242, 'g': 240, 'r': 134, 'rate': 1},
             '14': {'b': 18, 'g': 62, 'r': 182, 'rate': 1},
             '15': {'b': 91, 'g': 187, 'r': 228, 'rate': 3},
             '16': {'b': 212, 'g': 142, 'r': 51, 'rate': 3},
             '17': {'b': 125, 'g': 160, 'r': 218, 'rate': 3},
             '18': {'b': 80, 'g': 150, 'r': 46, 'rate': 1},
             '19': {'b': 137, 'g': 62, 'r': 77, 'rate': 2},
             '20': {'b': 214, 'g': 115, 'r': 182, 'rate': 3}
             }


class ML_Model:

    def __init__(self):
        try:
            self.res = requests.get(url="http://127.0.0.1:5000/b7438d633dd9915c")
            if self.res.status_code!=500:
                self.data = eval(self.res.content)
        except requests.exceptions.RequestException:  # This is the correct syntax
            self.data = {'1': {'b': 0, 'g': 0, 'r': 0, 'rate': 1}}

        self.r = None
        self.g = None
        self.b = None
        self.targets = None
        self.inputs = None

    def preprocess(self):
        red = list()
        green = list()
        blue = list()
        ratings = list()
        for color in list(self.data.values()):
            red.append(color['r'])
            green.append(color['g'])
            blue.append(color['b'])
            ratings.append([color['rate']])
        self.r = np.array(red)
        self.g = np.array(green)
        self.b = np.array(blue)
        self.targets = np.array(ratings)
        inp = list()
        inp.append(self.r)
        inp.append(self.g)
        inp.append(self.b)

        self.inputs = np.array(inp)
        self.inputs = self.inputs.reshape(self.inputs.shape[1], 3)

    def train(self):
        model = Pipeline([("scaler", MinMaxScaler(feature_range=(0, 1))),
                          ("liner_model", LinearRegression())])
        model.fit(self.inputs, self.targets)
        return model

    def predictor(self, r_c, g_c, b_c):
        self.preprocess()
        model = self.train()
        return model.predict([[r_c, g_c, b_c]])

