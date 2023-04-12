import json
import os

path_name = os.path.dirname(__file__)


class Levels:
    def __init__(self):
        self.levels = {}

        self.load_levels()

    def load_levels(self):
        with open(os.path.join(path_name, ".", "levels.json"), "r+", encoding="utf-8") as doc:
            all_levels = json.load(doc)
            for level in all_levels:
                name = level[0]
                matrix = level[1]
                self.levels[name] = matrix
