from __future__ import division
import math
#
# File: a02_stats.py
# your name: 
# your email:
# 
#

# write your functions here!

def calc_sum(a, b, c, d, e):

    # to do: implement this function and return a value!
    # do not print!

    return a+b+c+d+e

def calc_mean(a, b, c, d, e):
    return calc_sum(a, b, c, d, e)/5

def calc_variance(a, b, c, d, e):
    m = calc_mean(a, b, c, d, e)
    a2 = a-m
    b2= b-m
    c2= c-m
    d2= d-m
    e2= e-m
    return calc_mean(a2, b2, c2, d2, e2)

def calc_stdev(a, b, c, d, e):
    v =calc_variance(a, b, c, d, e)
    return v**.5
# THE SECTION BELOW CONTAINS THE TEST CODE FOR THE FUNCTIONS

# declare variables with which to test the functions
a = 8
b = 9
c = 10
d = 9
e = 8
# call the `calc_sum` function to calculate the sum of these 5 variables. 
# assign the result into a variable called `sum_of_obs`, and then print it out.
sum_of_obs = calc_sum(a, b, c, d, e) 
print("The sum of observations is:", sum_of_obs)

# continue to call your other functions below:
#print calc_mean(4,4,4,5,5)
#print calc_sum(-0.4,-0.4,-0.4,0.6,0.6)
#print calc_stdev(4,4,4,5,5)
#print calc_variance (4,4,4,5,5)
