###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")

q1 = codesters.Square(100, 100, 200, 'PapayaWhip')
q2 = codesters.Square(-100, -100, 200, 'PapayaWhip')
q3 = codesters.Square(-100, 100, 200, 'FloralWhite')
q4 = codesters.Square(100, -100, 200, 'FloralWhite')

cross = codesters.Sprite("image-removebg-preview.png", 100, 100)
cross.set_size(0.65)
volleyball = codesters.Sprite("volleyball for compthinking.png", 100, -100)
volleyball.set_size(0.15)
plane = codesters.Sprite("airplane.png", -100, 100)
plane.set_size(0.3)
shoes = codesters.Sprite("shoes.png", -100, -100)
shoes.set_size(0.4)

message1 = codesters.Text ("Nicola Grace Goncalves Williams",0,220,'Salmon')
message2 = codesters.Text ("Everything Happens For A Reason",0,-220,'White')