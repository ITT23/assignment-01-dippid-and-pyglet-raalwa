import pyglet


class Player:
    def __init__(self, x_position: int, radius: int, color: tuple[int, int, int], downward_acceleration: int = -10, y_position: int = 0):
        self.starting_y = y_position+radius
        self.player = pyglet.shapes.Circle(
            x_position, self.starting_y, radius, color=color)
        self.is_jumping = False
        self.acceleration = 0
        self.downward_acceleration = downward_acceleration
        self.starting_acceleration = 0

    def update(self):
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
            if self.player.y > self.starting_y:
                self.acceleration = self.downward_acceleration
            else:
                self.player.y = self.starting_y
                self.acceleration = 0
                self.is_jumping = False
