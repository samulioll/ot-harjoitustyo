import json
import os

level_path = os.path.dirname(__file__)[:-18] + "data/levels.json"


class Levels:
    """ A class that contains information about all of the levels. """

    def __init__(self):
        self.levels = {}
        self.load_levels()

    def load_levels(self):
        """ Loads level information from a .json file. """

        with open(level_path, "r+", encoding="utf-8") as doc:
            all_levels = json.load(doc)
            for level in all_levels:
                name = level[0]
                matrix = level[1]
                self.levels[name] = matrix

    def get_layout(self, level: int):
        """ Gets the layout matrix of the wanted level.

        Args:
            level (int): Selected level

            Returns:
                layout (list): The layout matrix of the level
        """

        return self.levels[str(level)]
