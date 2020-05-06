import math
import random

def calculate_projectile_distance(launch_angle, initial_velocity):
    x = (initial_velocity**2)/9.8
    y = math.sin(math.radians(2*launch_angle))
    return x*y

def calculate_launch_angle(distance, initial_velocity):
    x = 9.8*distance
    y = x/(initial_velocity**2)
    z = math.asin(y)
    return (z/2)
#problem with calculate launch angle
#possibly something to do with radians

if __name__ == '__main__':
    
    # print str(calculate_projectile_distance(25,50))
    print(str(calculate_launch_angle(250,50)))