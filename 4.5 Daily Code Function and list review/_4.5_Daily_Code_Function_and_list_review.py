import random
items = []
def itemDropper():
	chance = random.randint(0,100)
	if chance < 25:
		print("you got a potion!")
		items.append("potion")
	elif chance <50:
		print("you got a sock")
		items.append("sock")
	elif chance < 60:
		print("you got a coin")
		items.append("coin")
	else:
		print("you got nothing")

while True:
	input("")
	itemDropper()
	print(items)