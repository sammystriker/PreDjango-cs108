from __future__ import division
import math

def future_value(r, n, pv):
    return pv*((1+r)**n)


def present_value(r, n, fv):
    return fv/((1+r)**n)

def present_value_of_annuity(r, n, pmt):
    return ((1-((1+r)**-n))/r)*pmt

def annuity_payment(r, n, pv):
    t = r*pv
    d1 = (1+r)
    d2 = d1**(-n)
    d3 = 1- d2
    return t/d3

def dollar_format(amount):
    r = int(amount)
    s = str(r)
    return '$'+s
