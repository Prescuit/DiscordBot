import random
class ReactionClass:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def execute(self):
        if isinstance(self.data, list):
            i = random.randint(0, len(self.data)-1)
            return self.data[i]
        else:
            return self.data