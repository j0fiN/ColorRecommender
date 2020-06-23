class Data:
    def __init__(self):
        self.json = dict()

    def update(self, data):
        if len(list(self.json.keys())) == 0:
            self.json[1] = data
        else:
            self.json[list(self.json.keys())[-1] + 1] = data
