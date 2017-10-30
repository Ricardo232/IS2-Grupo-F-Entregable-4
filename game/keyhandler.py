import pygame as pg

class KeyHandler:

    def __init__(self):
        self.previous_key = ""
        self.move_keys = {"down": [0, 1, pg.K_DOWN],
                         "left": [-1, 0, pg.K_LEFT],
                         "up": [0, -1, pg.K_UP],
                         "right": [1, 0, pg.K_RIGHT]}

        self.vel_directions = {"down": [0, 1],
                               "downleft": [-1, 1],
                               "left": [-1, 0],
                               "upleft": [-1, -1],
                               "up": [0, -1],
                               "upright": [1, -1],
                               "right": [1, 0],
                               "downright": [1, 1]}

        self.move_key_combinations = ["downleft", "upleft", "upright", "downright"]
        self.move_keyspressed = []
        self.action_keys = {"q": pg.K_q}

    def get_key(self, n):
        i = -1
        for key in self.vel_directions:
            i += 1
            if i == n:
                return key

    def insert_key(self, key):
        counter = self.move_keyspressed.count(key)
        if counter == 0:
            self.move_keyspressed.append(key)

    def remove_key(self, key):
        counter = self.move_keyspressed.count(key)
        if counter == 1:
            self.move_keyspressed.remove(key)

    def check_keyorder(self, key1, key2):
        first_key = key1
        second_key = key2
        for value in self.move_key_combinations:
            if (first_key + second_key) == value:
                return first_key + second_key
            elif (second_key + first_key) == value:
                return second_key + first_key

        return first_key

    def get_move_direction(self):
        lenght = len(self.move_keyspressed)
        if lenght == 0:
            return self.previous_key
        if lenght == 1:
            first_key = self.move_keyspressed[lenght - 1]
            return first_key
        if lenght == 2:
            first_key = self.move_keyspressed[lenght - 1]
            second_key = self.move_keyspressed[lenght - 2]
            return self.check_keyorder(first_key, second_key)
        if lenght == 3:
            first_key = self.move_keyspressed[lenght - 1]
            second_key = self.move_keyspressed[lenght - 2]
            if first_key == self.check_keyorder(first_key, second_key):
                second_key = self.move_keyspressed[lenght - 3]
                return self.check_keyorder(first_key, second_key)

            return self.check_keyorder(first_key, second_key)
