import json
import os
import pygame as pg

path_name = os.path.dirname(__file__)

class Profile:
    """ Profile class containing relelvant info. """
    def __init__(self, username: str, scores: dict):
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
        saves = []
        with open(os.path.join(path_name, ".", "profiles.json"), "r") as document:
            all_profiles = json.load(document)
            for profile in all_profiles:
                username = profile[0]
                scores = profile[1]
                if username == self.username:
                    saves.append((self.username, self.scores))
                else:
                    saves.append((username, scores))
        with open(os.path.join(path_name, ".", "profiles.json"), "w") as document:
            json.dump(saves, document)

        
class AllProfiles:
    """ Class for the six save slots for profiles. """
    def __init__(self):
        self.profiles = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
        # Load profile info from .json file.
        with open(os.path.join(path_name, ".", "profiles.json"), "r+") as document:
            all_profiles = json.load(document)
            index = 1
            for profile in all_profiles:
                self.profiles[index] = Profile(profile[0], profile[1])
                index += 1
    
    def add_profile(self, username):
        """ Checks if a save slot is open and creates a profile if so. """
        index = 1
        for slot in self.profiles:
            if slot == None:
                self.profiles[index] = Profile(username, {})
                return True
            index += 1
        return False


    def delete_profile(self, index):
        """ Delete a profile. """
        pass

    #def update_scores(self, username, level, score):
     #   for slot, profile in self.profiles.items():
      #      if profile.username == username:
       #         profile.scores[level] = score
        

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

