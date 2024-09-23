# intro
print("it's christmas eve, and you can't sleep.")
print("as you're finally drifting off, you hear a funny noise from the roof")
print("suddenly, you hear a big thump and something that sounds like hooves")
print("you have to see what's going on. you have a gut feeling that something is up")
print("≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫≪ °❈° ≫")

# choice 1
print("")
c1 = input("do you climb onto the [roof], or do you try to see whats going on from the [yard]?")
if "roof" in c1:
    print("you walk out onto the balcony, and then quickly scale the side of your house, ignoring the snow.")

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
        print