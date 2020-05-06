# file: a11_date.py
# starter code by Aaron Stevens (azs@bu.edu)
# ## Sam Murray
#
# description: implementation of a Date class to represent a calendar date
# 

##########################################################################################
class Date:
    
    ##########################################################################################
    def __init__(self, month, day, year):
        '''Initialize this Date object.'''

        self.month = month
        self.day = day
        self.year = year

    ##########################################################################################
    def __repr__(self):
        '''Return a beautifully-formatted string representation 
        of this date as YY/MM/DD.'''

        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    # ##########################################################################################                    
    # def __eq__(self, other):
    #     '''Return True if both objects have the same month, day, year.'''
    #     return (self.year == other.year and
    #             self.month == other.month and
    #             self.day == other.day)
    
    ##########################################################################################
    def copy(self):
        '''Return a new Date object with the same 
        data attributes as this Date.'''

        d = Date(self.month, self.day, self.year)
        return d
        
    ##########################################################################################                    
    ## TO DO: Write your other methods here...

    def is_leap_year(self):
        






    
    ##########################################################################################                    
    # A fully-implemented diff method is provided. 
    # However, it will not work correctly until you
    # successfully implement the 'is_before', 'is_after', 
    # 'add_one_day' and 'rem_one_day' methods.
    def diff(self, other):
        '''Return the number of days between self and other.'''

        # if the two dates are 'equal', return a difference of 0 days.
        if self == other:
            return 0

        # create a copy of other, so as not to change the actual other object
        other = other.copy()

        MAX_DIFF = 10000 # upper bounds for the for loop

        # if the other Date comes before this Date, we will count up 
        # by adding one day at a time, until the two dates are 'equal'.
        if other.is_before(self):
            for i in range(1,MAX_DIFF):
                other.add_one_day()
                if other == self: 
                    return i

        # if the other Date comes after this Date, we will count down 
        # by removing one day at a time, until the two dates are 'equal'.
        elif other.is_after(self):
            for i in range(-1,-MAX_DIFF,-1):
                other.rem_one_day()
                if other == self: 
                    return i

        print("Error in diff method! self=%s, other=%s, i=%d" % (self, other, i))
        return i # Error case, should not happen



##########################################################################################                    
if __name__ == '__main__':

    ## TEST CODE HERE:
    # Use these date objects, or create your own. 
    # Uncomment lines below as needed.
    # Test every method thoroughly!

    d = Date(8,26,2001)
    print('d =', d)
    
    m1 = Date(4,20,2020)
    print('m1 =', m1)
    m2 = Date(4,20,2020)
    print("m2 = ", m2)

    # test for equality, and print out the result of the expression
    print('m1 == m2 evalutes to', m1 == m2)

    # d1 = Date(2,29,2020)
    # d2 = Date(3,1,2020)
    # d3 = Date(3,24,2019)
    # print("d1 =", d1)
    # print("d2 =", d2)
    # print("d3 =", d3)

    
    # print('d1.is_before(d2)', d1.is_before(d2))
    # print('d2.is_before(d1)', d2.is_before(d1))
    # print('d1.is_before(d3)', d1.is_before(d3))

    # A fully-implemented diff method is provided. 
    # However, it will not work correctly until you
    # successfully implement the 'is_before', 'is_after', 
    # 'add_one_day' and 'rem_one_day' methods.
    
    # print('d1.diff(d2)',d1.diff(d2))
    # print('d2.diff(d1)',d2.diff(d1))
    # print('m.diff(d1)',m.diff(d1))
    # print('d1.diff(d3)',d1.diff(d3))

