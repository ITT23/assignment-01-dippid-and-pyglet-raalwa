'''
This module defines the player character and its behaviour
'''
import pyglet


class Player:
    def __init__(self, x_position: int, downward_acceleration: int = -10, y_position: int = 0):
        image = pyglet.resource.image('resources/player.png')
        self.player = pyglet.sprite.Sprite(
            img=image, x=x_position, y=y_position)
        self.is_jumping = False
        self.acceleration = 0
        self.downward_acceleration = downward_acceleration
        self.starting_acceleration = 0
        self.is_game_over = False

    def update(self):
        if not self.is_game_over:
            self.player.y = self.player.y + self.acceleration
            self.update_acceleration()
        self.player.draw()

    def jump(self, acceleration: int):
        if not self.is_jumping:
            self.acceleration = acceleration
            self.starting_acceleration = acceleration
            self.is_jumping = True

    def update_acceleration(self):
        if self.acceleration > 0:
            self.acceleration = self.acceleration - 1
        else:
            if self.player.y > 0:
                self.acceleration = self.downward_acceleration
            else:
                self.player.y = 0
                self.acceleration = 0
                self.is_jumping = False

    def game_over(self):
        self.is_game_over = True
