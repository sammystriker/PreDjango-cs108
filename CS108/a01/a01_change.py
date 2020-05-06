# file: 
# author: 
#

# To make the autograder script work, you will need to follow these constraints:
# * You must have variables named price, change, quarters, dimes, nickels,
#   and pennies. You may include any additional variables you choose.
# * In your finished code, put all print statements at the bottom 
#   (as indicated by the comment).
#   You may use print statements elsewhere in your code while you are developing
#   and testing, but you should comment out those print statements before submission. 



# once you have a working solution, you should change this line to test other 
# starting values, e.g., 68 cents, 69 cents, etc. to ensure that your calculations 
# work for each value.
price = 67

# do all of your computations here:
ogchange = 100-price 
change = ogchange

quarters = change//25 
change = change- quarters*25

dimes = change//10
change = change - dimes*10

nickels = change//5
change = change - nickels*5

pennies = change

# put all print statements in this section:
print 'The price is', price,'cents. , and your change is ', change, 'cents.'   
print 'Here"s the change that uses the fewest coins'
print quarters, 'quarters,'
print dimes, 'dimes,'
print nickels, 'nickels, and '
print pennies, 'pennies'