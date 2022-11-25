from random import randrange

def draw_nums(num):
    rolls = []
    for x in range(0,num):
        rolls.append(randrange(1,7))
    return rolls