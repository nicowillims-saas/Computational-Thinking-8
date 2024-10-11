### NOTE: MY CODE IS WEIRD, SO IT DOESN'T WORK!



### SETUP ###
import codesters, random
from codesters import StageClass
stage = StageClass()
###############################################
t = codesters.Sprite("turtle",0, 0)

t.go_to(100, 0)
t.pen_down()
# t.set_speed(1000)
# stage.set_background_color( "white" )

#THE FIRST CIRCLE
colors = ["pink"]
for i in range(20):
    t.set_color(random.choice(colors))
    t.forward(150)
    t.turn_left(45 + 1)

#THE SECOND CIRCLE
t.pen_up()
t.go_to(0,0)
t.pen_down()
colors = ["green"]
for i in range(200):
    t.set_color(random.choice(colors))
    t.forward(150)
    t.turn_left(45 + 1)

