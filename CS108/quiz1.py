import math
import random

def cylinder_surface_area (x,y):
    return (2*math.pi*x*y) + (2*math.pi*(x**2))

def get_random_time():
    h = random.randint(0,23)
    m = random.randint(0,59)
    s = random.randint(0,59)
    if h<10:
         hs= '0'+__str__(h)
    else:
        hs =__str__(h)
        
    if m<10:
        ms= '0'+__str__(m)
    else:
        ms = __str__(m)
            
    if s<10:
        ss= '0'+__str__(s)
    else:
        ss=__str__(s)
    
    return (hs+':'+ms+':'+ss)

def facts_are_cool():
    print ("This program finds the factorial of a number.")
    input 
    return math.factorial(x)

def calculate_commission(sa,r):
    me=0
    if sa<1000000:
        me = sa*r
    
    if sa>1000000:
        nsa = sa-1000000
        if nsa>1000000:
            nsa=1000000
        me=(1000000*r)+(nsa*r*1.5)
 
    if sa>2000000:
        nnsa = sa-2000000
        me=(1000000*r)+(1000000*r*1.5)+(nnsa*r*2)

    return me

if __name__ == "__main__":
    print cylinder_surface_area(2,2)
    print calculate_commission(2500000,.02)
