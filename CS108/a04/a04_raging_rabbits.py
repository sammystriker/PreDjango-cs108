from a04_artillery_games import calculate_projectile_distance
from a04_artillery_games import calculate_launch_angle
import random

def raging_rabbits():
    iv = float(input('Enter your cannon\'s initial launch velocity (in m/s):'))
    long = calculate_projectile_distance(45,iv)
    short = calculate_projectile_distance(10,iv)

    print 'At an initial launch velocity of '+str(iv)+' meters/second, your cannon can hit a target between ' + str(short) +' and '+ str(long)+' meters.'

    rd = random.randint(int(short),int(long))

    print 'Your target is located at ' + str(rd) + ' meters.\n'
    guess = int(input('Enter your launch angle (in degrees):'))
    shot = calculate_projectile_distance(guess,iv)
    print 'Your projectile traveled '+str(shot)+' meters.'
    dif = rd-shot
    print 'Your shot was '+str(dif)+' meters from the target.'

if __name__ == '__main__':
    
    raging_rabbits()