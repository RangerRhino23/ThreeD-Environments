import random, os
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import assets.APIs.first_person_movement_api as fpm

directory = "assets/environments"
image_list = []

for filename in os.listdir(directory):
    if filename.endswith(".jfif"):
        image_list.append(filename)

def random_image():
    random_picture = random.choice(image_list)
    return random_picture

app = Ursina()

def update():
    player.position = (0,0,0)
    fpm.player_movement()

def input(key):
    if key == 'q':
        application.quit()
    if key == 'g':
        environment.texture = random_image()


player = FirstPersonController()
player.gravity = False

environment = Entity(model='sphere', scale=(-100,100,100), texture="assets\environments\house.jfif")

app.run()