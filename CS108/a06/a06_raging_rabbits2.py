from a04_artillery_games import * 

def raging_rabits2():
    print ("Welcome to Raging Rabbits!")
    cv = random.randint(100,200)
    print ("Your cannon has been calibrated with an initial launch velocity of "+ str(cv) +" meters/second.")
    short = int(calculate_projectile_distance(10,cv))
    long = int(calculate_projectile_distance(45,cv))

    print ("At this velocity, you can hit a target between " + str(short)+" and "+str(long)+" meters.")
    ran = (long - short)/20
    print("To succeed, you must land your bomb within "+ str(ran)+" meters of the target.")
    print()

    loc = random.randint(short,long)
    print("Your target is located "+str(loc)+ " meters away.")
    print("You get 5 tries to hit your target.")
    print()
    win = False
    for i in range(5):
        print("Attempt "+str(i))
        print()
        ang = int(input('Enter your launch angle (in degrees):'))
        shot = calculate_projectile_distance(ang,cv)
        print("Your projectile traveled "+str(shot)+" meters.")
        acc = loc-shot
        print("Your shot was "+str(acc)+" meters from the target")
        if abs(acc)<ran:
            win= True
        else:
            win = False
        
        if win == True:
            break

    if win == True:
        print("You hit your target!")
    else:
        print("You were not close enough to the target. :(")

if __name__ == '__main__':
    
    raging_rabbits2()   

