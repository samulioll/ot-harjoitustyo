import json
import os
import pygame as pg

path_name = os.path.dirname(__file__)


class Profile:
    """ Profile class containing relelvant info. """

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
        difficulty = difficulties[level // 10]
        return str(level), difficulty

    def update_scores(self, level, score):
        """ Updates the score list of the profile. """
        # Update profile within the game instance
        moves = score[0]
        time = score[1]
        try:
            new_moves = min(moves, self.scores[level][0])
            new_time = min(time, self.scores[level][1])
        except:
            new_moves = moves
            new_time = time
        self.scores[level] = (new_moves, new_time)
        # Update profiles json file
        saves = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
        with open(os.path.join(path_name, ".", "saves.json"), "r", encoding="utf-8") as doc:
            saves = json.load(doc)
            saves[self.slot] = [self.username, self.scores]
        with open(os.path.join(path_name, ".", "saves.json"), "w", encoding="utf-8") as doc:
            json.dump(saves, doc)

class AllProfiles:
    """ Class for the six save slots for profiles. """

    def __init__(self):
        self.profiles = {"1": None, "2": None,
                         "3": None, "4": None, "5": None, "6": None}
        # Load profile info from .json file.
        try:
            with open(os.path.join(path_name, ".", "saves.json"), "r+", encoding="utf-8") as doc:
                all_profiles = json.load(doc)
                for slot, profile in all_profiles.items():
                    try:
                        self.profiles[slot] = Profile(
                            slot, profile[0], profile[1])
                    except:
                        pass
        except:
            with open(os.path.join(path_name, ".", "saves.json"), "w", encoding="utf-8") as doc:
                json.dump(self.profiles, doc)

    def add_profile(self, username):
        """ Checks if a save slot is open and creates a profile if so. """
        for slot, profile in self.profiles.items():
            if profile is None:
                new_profile = Profile(slot, username, {})
                self.profiles[slot] = new_profile
                with open(os.path.join(path_name, "saves.json"), "r", encoding="utf-8") as doc:
                    saves = json.load(doc)
                    saves[slot] = [username, {}]
                with open(os.path.join(path_name, "saves.json"), "w", encoding="utf-8") as doc:
                    json.dump(saves, doc)
                return new_profile

    def delete_profile(self, slot):
        """ Delete a profile. """
        self.profiles[slot] = None
        with open(os.path.join(path_name, ".", "saves.json"), "r", encoding="utf-8") as doc:
            saves = json.load(doc)
            saves[slot] = None
        with open(os.path.join(path_name, ".", "saves.json"), "w", encoding="utf-8") as doc:
            json.dump(saves, doc)

class InputBox:
    def __init__(self, x_coord, y_coord, width, height, text=""):
        self.font = pg.font.SysFont("Arial", 50)
        self.rect = pg.Rect(x_coord, y_coord, width, height)
        self.color = (0, 0, 0)
        self.text = text
        self.text_surface = self.font.render(text, True, self.color)


    def input_handler(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                return self.text
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.text_surface = self.font.render(
                self.text, True, self.color)

    def draw(self, surface):
        pg.draw.rect(surface, (231, 203, 233), self.rect, 25)
        pg.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.text_surface, (self.rect.x+5, self.rect.y-3))
