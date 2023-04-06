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
        return str(len(self.scores) + 1)
    
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
        with open(os.path.join(path_name, ".", "profiles.json"), "r") as document:
            saves = json.load(document)
            saves[self.slot] = [self.username, self.scores]
        with open(os.path.join(path_name, ".", "profiles.json"), "w") as document:
            json.dump(saves, document)

        
class AllProfiles:
    """ Class for the six save slots for profiles. """
    def __init__(self):
        self.profiles = {"1": None, "2": None, "3": None, "4": None, "5": None, "6": None}
        # Load profile info from .json file.
        with open(os.path.join(path_name, ".", "profiles.json"), "r+") as document:
            all_profiles = json.load(document)
            for slot, profile in all_profiles.items():
                try:
                    self.profiles[slot] = Profile(slot, profile[0], profile[1])
                except:
                    pass
    
    def add_profile(self, username):
        """ Checks if a save slot is open and creates a profile if so. """
        for slot, profile in self.profiles.items():
            if profile == None:
                new_profile = Profile(slot, username, {})
                self.profiles[slot] = new_profile
                with open(os.path.join(path_name, ".", "profiles.json"), "r") as document:
                    saves = json.load(document)
                    saves[slot] = [username, {}]
                with open(os.path.join(path_name, ".", "profiles.json"), "w") as document:
                    json.dump(saves, document)
                return new_profile

    def delete_profile(self, slot):
        """ Delete a profile. """
        self.profiles[slot] = None
        with open(os.path.join(path_name, ".", "profiles.json"), "r") as document:
            saves = json.load(document)
            saves[slot] = None
        with open(os.path.join(path_name, ".", "profiles.json"), "w") as document:
            json.dump(saves, document)

    def draw_users(self, active_color, passive_color):
        """ Returns a list of pygame text objects of all profiles and empty slots. """
        usernames = []
        font = pg.font.SysFont("Arial", 50)
        y = 450
        for slot, profile in self.profiles.items():
            if profile == None:
                text = font.render("EMPTY SLOT", True, (passive_color, passive_color, passive_color), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y
                usernames.append((text, text_rect))
            else:
                text = font.render(profile.username, True, (active_color, active_color, active_color), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y
                usernames.append((text, text_rect))
            y += 100
        return usernames

class InputBox:
    def __init__(self, x, y, w, h, text=""):
        self.font = pg.font.SysFont("Arial", 50)
        self.rect = pg.Rect(x,y,w,h)
        self.color = (0,0,0)
        self.text = text
        self.text_surface = self.font.render(text, True, self.color)
        self.active = False

    def input_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    return self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface = self.font.render(self.text, True, self.color)
    
    def draw(self, surface):
        pg.draw.rect(surface, (231,203,233), self.rect, 25)
        pg.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.text_surface, (self.rect.x+5, self.rect.y-3))