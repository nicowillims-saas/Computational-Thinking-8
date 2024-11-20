# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("project5bg.jpg")


player = codesters.Sprite("gingerbread.png")
player.set_size(0.5)
player.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 5


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("present", x_position, 250)
        object.set_size(0.1)
        object.set_y_speed(-5)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "present.png":
        stage.remove_sprite("s2")
        if lives == 0:
            print("test")
        else:
            print("test")
             
player.event_collision(collision)




# Section 4 - Controls
def move_left(sprite):
    sprite.move_left (4)
def move_right(sprite):
    sprite.move_right (4)
player.event_key("a", move_left)
player.event_key("d", move_right)