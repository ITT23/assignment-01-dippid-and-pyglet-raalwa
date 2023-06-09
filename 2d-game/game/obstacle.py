'''
This module defines the obstacle and its behaviour
'''
import pyglet
import random


class Obstacle():
    def __init__(self, x_position: int, speed: int, y_position: int = 0):
        image = pyglet.resource.image('resources/obstacle.png')
        self.obstacle = pyglet.sprite.Sprite(
            img=image, x=x_position, y=y_position)
        self.starting_x = x_position
        self.speed = speed
        self.is_game_over = False
        self.score = 0

    def update(self):
        if not self.is_game_over:
            self.obstacle.x = self.obstacle.x - self.speed
            self.check_position()
        self.obstacle.draw()

    def check_position(self):
        if (self.obstacle.x + self.obstacle.width) < 0:
            self.score += 1
            self.obstacle.x = self.starting_x
            # self.obstacle.height = random.randrange(100, 400)
            self.obstacle.update(scale_y=1+(round(random.random(), 2)*4))

    def game_over(self):
        self.is_game_over = True
