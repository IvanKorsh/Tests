import random


def coin_flip(n):
    rez = []
    centre = 0.5

    for num in range(n):
        flip = random.randint(0, 1)
        if flip == 0:
            rez.append("T")
        else:
            rez.append("H")

    print(rez)

def probability():
