import random

def hit(AR, DR, AL, DL):
    n = random.random()
    chance = 2 * (AR/(AR + DR)) * (AL/(AL + DL))
    if chance > 1:
        chance = 1
    if n <= chance:
        return True
    else:
        return False

def block(BR):
    n = random.random()
    if n <= BR:
        return True
    else:
        return False



'''
Abbreviations:
AR = Attacker's Attack Rating
DR = Defender's Defense rating
Alvl = Attacker's level
Dlvl = Defender's level
BR = Block Rate
'''
