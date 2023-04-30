import pyglet
import ast
from game import player, obstacle
from resources.DIPPID import SensorUDP
import resources.constants as constants

sensor = SensorUDP(constants.PORT)
window = pyglet.window.Window(
    width=constants.WINDOW_WIDTH,
    height=constants.WINDOW_HEIGHT)

this_obstacle = obstacle.Obstacle(
    x_position=constants.WINDOW_WIDTH,
    height=100,
    width=constants.OBSTACLE_WIDTH,
    color=constants.OBSTACLE_COLOR)

this_player = player.Player(
    x_position=constants.PLAYER_STARTING_POINT,
    radius=constants.PLAYER_RADIUS,
    color=constants.PLAYER_COLOR)

score = 0


def handle_input():
    if sensor.has_capability('accelerometer'):
        acceleration_z = float(ast.literal_eval(
            sensor.get_value('accelerometer'))['z'])
        if acceleration_z > 0.6:
            this_player.jump(int(acceleration_z*constants.MAX_ACCELERATION))


def check_colission():
    player_position_y = this_player.player.y
    obstacle_position = this_obstacle.obstacle.x

    obstacle_x = obstacle_position + this_obstacle.obstacle.width/2
    x_distance = abs(constants.PLAYER_STARTING_POINT - obstacle_x)
    player_y = player_position_y - this_player.player.radius

    if x_distance <= (this_player.player.radius + this_obstacle.obstacle.width/2) and player_y <= this_obstacle.obstacle.height:
        print("Colission")
    else:
        print("No colission")


def update_score():
    pass


@window.event
def on_draw():
    window.clear()
    check_colission()
    update_score()
    handle_input()
    this_obstacle.update()
    this_player.update()


# @window.event
# def on_key_press(symbol, modifier):
#     if (symbol == key.Q):
#         print("Q pressed")


if __name__ == '__main__':
    pyglet.app.run()
