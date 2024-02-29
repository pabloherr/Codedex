
from math import pi
from random import choices, choice
from random import choice as ch

def slot():
    l = ['C','U','S','7']
    results = choices(l,k = 3)
    if results[0] == results[1] and results[1] == results[2]:
        return str(results) + '\n Jackpot!'
    return results

print(slot())

def area():
    planets_l = [  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn']
    planets_d = {
  'Mercury':2440,
  'Venus':6052,
  'Earth':6371,
  'Mars':3390,
  'Saturn':58232
    }
    planet = ch(planets_l)
    planet_r = planets_d.get(planet)
    planet_a = 4*pi*planet_r**2
    return {planet:planet_a}

print(area())