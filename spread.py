"""
Market or Risky Price = sum(1 to n)((CF_1to_n)/(1+(r+s)/m)^nm))

Author: Oluwaseyi Awoga
IDE: CS50 IDE on Cloud 9/AWS
Topic: Optimization of SOFR Spread Adjustment Calculation
Location: Milky-Way Galaxy
"""

#from datetime import date
from numpy import array
import numpy as np
from scipy.optimize import fsolve


mktPrice = 98
maturity = 2
r = 0.05  #risk free rate
par = 100
numberOfPymntsPerYear = 4
notional = 1000000000
start = 0
numberOfTotalPymnts = 8

def zSpread(spread):
    discountedValue= 0
    s = spread[0]
    timeElapsed = 0
    for x in range(1,8):
        timeElapsed = timeElapsed + 3
        print(x)
        quarterlyInterest = 3/12 * r * notional
        temp = quarterlyInterest/(1+(r+s)**(timeElapsed))
        discountedValue = discountedValue + temp




    return discountedValue

print(zSpread([0.0]))

# def optimizationfunc([0]):

#     a = mktPrice
#     b = zSpread(spread)

#     return a - b


# solutions = fsolve(optimizationfunc,[0.4/100],xtol=1.49012e-08,)
# spreadtoUse = solutions[0]

