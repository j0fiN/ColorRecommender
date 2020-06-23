class Data:
    def __init__(self):
        self.json = {0: {'r': 0, 'g': 0, 'b': 0, 'rate': 1},
                     1: {'r': 255, 'g': 255, 'b': 255, 'rate': 3}}

    def update(self, data):
        if len(list(self.json.keys())) == 0:
            self.json[1] = data
        else:
            self.json[list(self.json.keys())[-1] + 1] = data
