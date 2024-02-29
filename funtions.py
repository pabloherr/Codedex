import random

def fortune():
    i = random.randint(0,7)
    l = ['Dont pursue happiness - create it.',
        'All things are difficult before they are easy.',
        'The early bird gets the worm, but the second mouse gets the cheese.',
        'Someone in your life needs a letter from you.',
        'Dont just think. Act!',
        'Your heart will skip a beat.',
        'The fortune you search for is in another cookie.',
        'Help! Im being held prisoner in a Chinese bakery!']
    return (l[i])
print(fortune())

def distance_to_miles(km:int):
    return km/1.609

print(distance_to_miles(10000))

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x:int):
    x -=1
    return stock_prices[x]

def max_price(a:int,b:int):
    a -= 1
    l = stock_prices[a:b]
    return max(l)

def min_price(a:int,b:int):
    a -= 1
    l = stock_prices[a:b]
    return min(l)

print(price_at(4))
print(max_price(1,4))
print(min_price(1,4))