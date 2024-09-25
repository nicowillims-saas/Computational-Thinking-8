# intro
print("it's christmas eve, and you can't sleep.")
print("as you're finally drifting off, you hear a funny noise from the roof")
print("suddenly, you hear a big thump and something that sounds like hooves")
print("you have to see what's going on. you have a gut feeling that something is up")
print("≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫")

# choice 1
print("")
print("you can't just pretend you didn't hear hooves on the roof- you rush out to the side of your house to get to the roof.")

# choice 2
print("as you get to the top of your house, nothing is there. however, you do notice footprints that continue off the roof, as if someone jumped off in a hurry.")
print("what's going on!?")
c2 = input("do you [follow the footprints] or [take a closer look at the roof]?")
if "follow" in c2 or "footprint" in c2:
    print("you rush down to the backyard, where the footprints continue. you walk alongside the footprints, and suddenly you realize that you aren't in your fenced in yard anymore, you're in a forest of christmas trees!")
    print("as you spin around, somehow your house is nowhere in sight. the only thing you see is a bright light at the very end of the forest!")
    print("you sigh, and continue your walk through the snowy forest")
if "closer look" in c2 or "roof" in c2:
    print ("you decide that there are probably more clues up on the roof. so you rush back inside to grab a flashlight, then run back out to investigate further.")
    print ("after exploring for a few more minutes, you see a basket on the chimney. inside is a bag of candy canes and a letter with a messy signature at the bottom.")        
    print ("the letter says:")
    print ("to whoever finds this, please help! the easter bunny got jealous that people liked my holiday better, and he kidnapped me so people forget about christmas! please save me, or else christmas is CANCELLED!!!")
    print ("you think, and have three plans in mind. first, you could go back to [sleep] and forget everything that happened. second, you could go back and investigate the [footprints]. third, you could investigate the bag of [candy canes].")

# choice 3
c3 = input("do you want to [sleep], explore the [footprints], or investigate the [candy canes]?")
if "sleep" in c2:
    print("you go back to sleep, and the next day there is no christmas! you try to report the easter rabbit to the authorities but they dont believe you. 100 years later, nobody remembers christmas anymore.")
elif "roof" in c2:
    print("you rush down to the backyard, where the footprints continue. you walk alongside the footprints, and suddenly you realize that you aren't in your fenced in yard anymore, you're in a forest of christmas trees!")
    print("as you spin around, somehow your house is nowhere in sight. the only thing you see is a bright light at the very end of the forest!")
    print("you sigh, and continue your walk through the snowy forest")
else:
    print("you open the bag of candy canes, and you're so hungry that you take a bite out of one. suddenly, your head starts spinning and you feel like you're falling.")
    print("all of a sudden, you wake up and the easter bunny is grinning and tying santa to an easter egg")
    print("you realize the bunny's plan- he's keeping santa in his evil lair so eventually everybody will forget about christmas and focus on easter!")
    print("the easter bunny looks over at you and says...")
    print("I see you have realized my evil plan- if you can pick the right egg, then I will release you and santa.")
c2 = input
