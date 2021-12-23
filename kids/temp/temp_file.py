import random as rnd

some_data = [x*rnd.randint(100, 200) for x in range(10)]

with open('readme.txt', "a") as f:
    f.write(str(some_data))

with open('readme.txt', 'r') as f:
    print(f.read())


