import json
import os
import pygame as pg

save_path = os.path.dirname(__file__)[:-18] + "data/saves.json"


class Profile:
    """ A class for a single profile containing relevant info. 
        
        Attributes:
            slot (int): The save slot of the profile (1-6)
            username (str): The username of the profile
            scores (dict): A dictionary of all solved levels and their scores. 
    """

    def __init__(self, slot: int, username: str, scores: dict):
        self.slot = slot
        self.username = username
        self.scores = scores

    def current_level(self):
        """ Returns the next unsolved level. """

        level = len(self.scores) + 1
        difficulties = {0: "Beginner",
                        1: "Easy",
                        2: "Medium",
                        3: "Advanced",
                        4: "Hard"}
        difficulty = difficulties[(level - 1) // 10]
        return level, difficulty

    def update_scores(self, level: int, score: int):
        """ Updates the score list of the profile.

        Args:
            level (int): Selected level.
            score (int): Move count.
        """

        moves = score
        try:
            new_moves = min(moves, self.scores[level])
        except KeyError:
            new_moves = moves
        self.scores[level] = new_moves
        saves = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
        with open(save_path, "r", encoding="utf-8") as doc:
            saves = json.load(doc)
            saves[self.slot] = [self.username, self.scores]
        with open(save_path, "w", encoding="utf-8") as doc:
            json.dump(saves, doc)


class AllProfiles:
    """ A class for the six save slots for profiles. """

    def __init__(self):
        self.profiles = {"1": None, "2": None,
                         "3": None, "4": None, "5": None, "6": None}
        try:
            with open(save_path, "r+", encoding="utf-8") as doc:
                all_profiles = json.load(doc)
                for slot, profile in all_profiles.items():
                    try:
                        self.profiles[slot] = Profile(
                            slot, profile[0], profile[1])
                    except TypeError:
                        pass
        except FileNotFoundError:
            with open(save_path, "w", encoding="utf-8") as doc:
                json.dump(self.profiles, doc)

    def add_profile(self, username: str):
        """ Checks if a save slot is open and creates a profile if so.

        Args:
            username (str): Wanted username

        Returns:
            Profile: A profile object with given username and slot.
        """

        for slot, profile in self.profiles.items():
            if profile is None:
                new_profile = Profile(slot, username, {})
                self.profiles[slot] = new_profile
                with open(save_path, "r", encoding="utf-8") as doc:
                    saves = json.load(doc)
                    saves[slot] = [username, {}]
                with open(save_path, "w", encoding="utf-8") as doc:
                    json.dump(saves, doc)
                return new_profile
        return None

    def delete_profile(self, slot: int):
        """ Delete a profile from a slot.

        Args:
            slot (int): The selected slot to be cleared
        """

        self.profiles[slot] = None
        with open(save_path, "r", encoding="utf-8") as doc:
            saves = json.load(doc)
            saves[slot] = None
        with open(save_path, "w", encoding="utf-8") as doc:
            json.dump(saves, doc)


class InputBox:
    """ A class for an input box for writing a username for a new profile. 
        
        Attributes:
            x_coord (int): X-coordinate of the input box.
            y_coord (int): Y-coordinate of the input box.
            width (int): Width of the input box.
            height (int): Height of the input box.
    """

    def __init__(self, x_coord: int, y_coord: int, width: int, height: int, text=""):
        self.font = pg.font.SysFont("Arial", 50)
        self.rect = pg.Rect(x_coord, y_coord, width, height)
        self.color = (0, 0, 0)
        self.text = text
        self.text_surface = self.font.render(text, True, self.color)

    def input_handler(self, event):
        """ Adds letters to the input box and returns them when ENTER
            is pressed.

        Args:
            event: Pygame event

        Returns:
            Given username if ENTER is pressed.
        """

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                return self.text
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) <= 9:
                self.text += event.unicode
            self.text_surface = self.font.render(
                self.text, True, self.color)
        return None

    def draw(self, surface):
        """ Draws the input box.

        Args:
            surface: The given surface to draw the box onto.
        """

        pg.draw.rect(surface, (231, 203, 233), self.rect, 40)
        pg.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.text_surface, (self.rect.x+10, self.rect.y+10))
