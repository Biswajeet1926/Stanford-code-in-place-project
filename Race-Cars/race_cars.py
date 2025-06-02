from ursina import *
import random

def update():
    global offset, game_over
    if game_over:
        return  # stop game logic if game over

    offset += time.dt * .3
    setattr(track, "texture_offset", (0, offset))

    car0.x += held_keys['d'] * time.dt * .2
    car0.x -= held_keys['a'] * time.dt * .2

    if car0.x >= .24:
        car0.x = .24
    if car0.x <= -.28:
        car0.x = -.28

    for car in cars:
        if car.rotation_y == 0:
            car.z -= time.dt * random.uniform(.02, .05)
        else:
            car.z -= time.dt * random.uniform(.09, .12)

        if car.z < -.3:
            car.z = .4

        if abs(car0.x - car.x) < .05 and abs(car0.z - car.z) < .05:
            trigger_game_over()

def trigger_game_over():
    global game_over
    if not game_over:
        game_over = True
        car0.rotation_y = 0
        game_over_text.enabled = True
        bg_music.stop()
        Audio('assets/game_over.mp3', autoplay=True)

class Car(Entity):
    scale_y = .0001
    scale_z = .06
    def __init__(self, img, scale_x, position, angle):
        super().__init__()
        self.parent = track
        self.model = "cube"
        self.texture = img
        self.scale = (scale_x, self.scale_y, self.scale_z)
        self.position = position
        self.collider = "box"
        self.rotation_y = angle

# Game Init
app = Ursina()
window.color = color.orange
offset = 0
game_over = False

# Load Background Music (Loop)
bg_music = Audio('assets/bg_music.mp3', loop=True, autoplay=True)

# Scene Setup
cars_img = ["assets/car0.png", "assets/car1.png", "assets/car2.png", "assets/car3.png", "assets/car4.png"]
track = Entity(model='cube', color=color.green, scale=(10, .5, 60), position=(0,0), texture="assets/track.png")

car0 = Car(cars_img[0], 0.15, (.05, 1, -.12), 0)
car1 = Car(cars_img[1], 0.08, (.05, 1, .2), 0)
car2 = Car(cars_img[2], 0.07, (.19, 1, .1), 0)
car3 = Car(cars_img[3], 0.07, (-.09, 1, 0), 180)
car4 = Car(cars_img[4], 0.07, (-.23, 1, -.1), 180)
cars = [car1, car2, car3, car4]

# Game Over UI
game_over_text = Text("GAME OVER", origin=(0,0), scale=2, color=color.red, enabled=False)

camera.position = (0,8,-26)
camera.rotation_x = 20

app.run()
