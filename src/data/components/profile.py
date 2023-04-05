import json
import os
import pygame as pg

path_name = os.path.dirname(__file__)

class Profile:
    def __init__(self, username: str, scores: dict):
        self.username = username
        self.scores = scores


class AllProfiles:
    def __init__(self):
        self.profiles = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}

        with open(os.path.join(path_name, ".", "profiles.json"), "r+") as document:
            all_profiles = json.load(document)
            index = 1
            for profile in all_profiles:
                self.profiles[index] = Profile(profile[0], profile[1])
                index += 1
    

    def add_profile(self, username):
        index = 1
        for slot in self.profiles:
            if slot == None:
                self.profiles[index] = Profile(username, {})
                return True
            index += 1
        return False


    def delete_profile(self, index):
        pass


    def draw_users(self, color):
        usernames = []

        font = pg.font.SysFont("Arial", 50)
        y = 450
        empties = 0
        for slot, profile in self.profiles.items():
            empties += 1 if not profile else 0
        for slot, profile in self.profiles.items():
            if profile == None:
                continue
            text = font.render(profile.username, True, (color, color, color), None)
            text_rect = text.get_rect()
            text_rect.x = 625
            text_rect.y = y
            usernames.append((text, text_rect))
            y += 100
        if empties:
            for i in range(empties):
                text = font.render("EMPTY SLOT", True, (color, color, color), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y
                usernames.append((text, text_rect))
                y += 100     
        return usernames


def load_profiles():
    profiles = []
    with open(os.path.join(path_name, ".", "profiles.json"), "r+") as document:
        all_profiles = json.load(document)
        for profile in all_profiles:
            username = profile[0]
            scores = profile[1]
            curr_profile = Profile(username, scores)
            profiles.append(curr_profile)
    return profiles
