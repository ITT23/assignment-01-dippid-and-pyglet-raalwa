'''
This module starts the game

Pyglet UI and general game logic is handled here
This project is roughly based on
- https://pyglet.readthedocs.io/en/latest/programming_guide/examplegame.html
- https://github.com/pyglet/pyglet/tree/master/examples/game
'''
import pyglet
from game import player, obstacle
from resources.DIPPID import SensorUDP
from resources import constants

sensor = SensorUDP(constants.PORT)
window = pyglet.window.Window(
    width=constants.WINDOW_WIDTH,
    height=constants.WINDOW_HEIGHT)
background_image = pyglet.resource.image('resources/background.png')


def init():
    '''
    Initializes player, obstacle and UI elements
    '''
    global this_player, this_obstacle, score, score_display,\
        background, game_over_display

    this_player = player.Player(x_position=constants.PLAYER_STARTING_POINT)

    this_obstacle = obstacle.Obstacle(
        x_position=constants.WINDOW_WIDTH, speed=constants.OBSTACLE_SPEED)

    score = this_obstacle.score

    score_display = pyglet.text.Label(text=f"Score: {score}",
                                      font_size=25,
                                      x=10,
                                      y=constants.WINDOW_HEIGHT-50,
                                      color=constants.TEXT_COLOR)

    game_over_display = pyglet.text.Label(text="",
                                          font_size=20,
                                          anchor_x='center',
                                          x=int(constants.WINDOW_WIDTH/2),
                                          y=int(constants.WINDOW_HEIGHT/2),
                                          multiline=True,
                                          width=325,
                                          align='center',
                                          color=constants.TEXT_COLOR)

    background = pyglet.sprite.Sprite(img=background_image)


def handle_input():
    '''
    Listens to accelerometer z axis and makes player jump if threshold is overcome
    '''
    if sensor.has_capability('accelerometer'):
        acceleration_z = float(sensor.get_value('accelerometer')['z'])
        if acceleration_z > constants.JUMPING_THRESHOLD:
            this_player.jump(int(acceleration_z*constants.MAX_ACCELERATION * 2))


def check_colission():
    '''
    Checks whether player and obstacle have collided

    Returns:
        True: for collision
        False: for avoidance
    '''
    obstacle_x = this_obstacle.obstacle.x + this_obstacle.obstacle.width/2
    player_x = constants.PLAYER_STARTING_POINT + this_player.player.width/2
    x_distance = abs(player_x - obstacle_x)

    return x_distance <= (this_player.player.width/2 + this_obstacle.obstacle.width/2) and this_player.player.y <= this_obstacle.obstacle.height


def update_score():
    '''
    Updates score display to show current score
    '''
    score_display.text = f"Score: {this_obstacle.score}"
    score_display.draw()


def handle_restart():
    '''
    Listens to button_1 press and restarts game accordingly
    '''
    if sensor.has_capability('button_1'):
        button_state = sensor.get_value('button_1')
        if button_state == 1:
            init()


def show_endscreen():
    '''
    Displays game over screen with final score
    '''
    game_over_display.text = f"Your final score was: {this_obstacle.score} Press Button 1 to start again"
    game_over_display.draw()


@window.event
def on_draw():
    '''
    Handler for pyglet.windows.on_draw() event
    '''
    window.clear()
    background.draw()
    if check_colission():
        this_obstacle.game_over()
        this_player.game_over()
        handle_restart()
        show_endscreen()
    handle_input()
    this_obstacle.update()
    this_player.update()
    update_score()


if __name__ == '__main__':
    init()
    pyglet.app.run()
