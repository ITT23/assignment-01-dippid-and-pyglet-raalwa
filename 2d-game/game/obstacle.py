import pyglet


class Obstacle():
    def __init__(self, x_position: int, height: int, color: tuple[int, int, int], width: int, speed: int = 2, y_position: int = 0):
        self.obstacle = pyglet.shapes.Rectangle(
            x=x_position, y=y_position, width=width, height=height, color=color)
        self.starting_x = x_position
        self.speed = speed

    def update(self):
        self.obstacle.x = self.obstacle.x - self.speed
        self.check_position()
        self.obstacle.draw()

    def check_position(self):
        if (self.obstacle.x + self.obstacle.width) < 0:
            self.obstacle.x = self.starting_x
