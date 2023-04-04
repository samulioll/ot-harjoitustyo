import json

class Levels:
    def __init__(self):
        self.levels = {}
        
        self.load_levels()

    def load_levels(self):
        with open("levels.json", "r+") as document:
            all_levels = json.load(document)
            for level in all_levels:
                name = level[0]
                matrix = level[1]
                self.levels[name] = matrix
