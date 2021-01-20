import random

health = 50

difficulty = 1

potion_health_medium = int(random.randint(25,50) / difficulty)

health = health + potion_health_medium

potion_poison_small = random.randint(5,15)

health = health - potion_poison_small
print (health)
print (potion_health_medium)
print (potion_poison_small)
