import pyglet
from game import player, obstacle
from resources.DIPPID import SensorUDP
import resources.constants as constants

sensor = SensorUDP(constants.PORT)
window = pyglet.window.Window(
    width=constants.WINDOW_WIDTH,
    height=constants.WINDOW_HEIGHT)
background_image = pyglet.resource.image('resources/background.png')

def init():
    global this_player, this_obstacle, score, score_display, background

    this_player = player.Player(
        x_position=constants.PLAYER_STARTING_POINT,
        radius=constants.PLAYER_RADIUS,
        color=constants.PLAYER_COLOR)
    
    this_obstacle = obstacle.Obstacle(
        x_position=constants.WINDOW_WIDTH,
        height=100,
        width=constants.OBSTACLE_WIDTH,
        color=constants.OBSTACLE_COLOR)
    
    score = this_obstacle.score

    score_display = pyglet.text.Label(text=f"Score: {score}",
                                      font_size=25,
                                      x=10,
                                      y=constants.WINDOW_HEIGHT-50)
    
    background = pyglet.sprite.Sprite(img=background_image)

def handle_input():
    if sensor.has_capability('gyroscope'):
        acceleration_z = float(sensor.get_value('gyroscope')['z'])
        if acceleration_z > 0.6:
            this_player.jump(int(acceleration_z*constants.MAX_ACCELERATION))


def check_colission():
    obstacle_x = this_obstacle.obstacle.x + this_obstacle.obstacle.width/2
    player_y = this_player.player.y - this_player.player.radius
    x_distance = abs(constants.PLAYER_STARTING_POINT - obstacle_x)

    return False
    return x_distance <= (this_player.player.radius + this_obstacle.obstacle.width/2) and player_y <= this_obstacle.obstacle.height


def update_score():
    score_display.text = f"Score: {this_obstacle.score}"

def handle_restart():
    if sensor.has_capability('button_1'):
        button_state = sensor.get_value('button_1')
        if button_state == 1:
            init()

@window.event
def on_draw():
    window.clear()
    background.draw()
    if check_colission():
        this_obstacle.game_over()
        this_player.game_over()
        handle_restart()
        # show endscreen with final score
    update_score()
    handle_input()
    this_obstacle.update()
    this_player.update()
    score_display.draw()


if __name__ == '__main__':
    init()
    pyglet.app.run()
