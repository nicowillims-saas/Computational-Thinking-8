# Beginning: create variables
xmas_points = 0
hw_points = 0
bday_points = 0
thx_points = 0
july_points = 0


# Middle: Ask questions
# question 1:
answer = input("on a weekend, would you rather: a) go sledding, b) go to a pumpkin patch, c) bake a cake, d) have a meal with extended family, or e) set off fireworks")
if answer == "A":
	xmas_points += 1
elif answer == "B":
	hw_points += 1
elif answer == "C":
	bday_points += 1
elif answer == "D":
	thx_points += 1
else:
	july_points += 1


# question 2:
answer = input("pick a color combo: a) red and green, b) orange and black, c) red, yellow, and blue, d) red, brown, and orange, e) red, white, and blue")
if answer == "A":
	xmas_points += 1
elif answer == "B":
	hw_points += 1
elif answer == "C":
	bday_points += 1
elif answer == "D":
	thx_points += 1
else:
	july_points += 1
	
# question 3
answer = input("pick a song: a) holly jolly christmas, b) monster mash, c) happy birthday, d) thanksgiving song, e) party in the USA")
if answer == "A":
	xmas_points += 1
elif answer == "B":
	hw_points += 1
elif answer == "C":
	bday_points += 1
elif answer == "D":
	thx_points += 1
else:
	july_points += 1

# question 4
answer = input("what's your favorite time of year? a) middle of winter, b) middle of fall, c) any time!, d) end of fall e) middle of summer")
if answer == "A":
	xmas_points += 1
elif answer == "B":
	hw_points += 1
elif answer == "C":
	bday_points += 1
elif answer == "D":
	thx_points += 1
else:
	july_points += 1

# question 5
answer = input("what's your favorite way of celebrating: a) gift giving, b) dressing up, c) sweet treats and presents, d) a big feast e) staying up late and fireworks")
if answer == "A":
	xmas_points += 1
elif answer == "B":
	hw_points += 1
elif answer == "C":
	bday_points += 1
elif answer == "D":
	thx_points += 1
else:
	july_points += 1


# End: determine results
if xmas_points > 2:
	print("you are a christmas person")
elif hw_points > 2:
	print("You are a halloween person")
elif bday_points > 2:
	print("You are a birthday person")
elif thx_points > 2:
	print("You are a thanksgiving person")
elif july_points > 2:
	print("you are a fourth of july person")
else:
	print("you are a mix!")