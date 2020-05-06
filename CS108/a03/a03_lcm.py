from a03_tvm import present_value_of_annuity
from a03_tvm import annuity_payment
from a03_tvm import dollar_format

def life_cycle_model():
    rr = float(input('Enter the current inflation-indexed risk-free rate of return:'))
    age = int(input('Enter your age now:'))
    ret = int(input('Enter your expected retirement age:'))
    ci = int(input('Enter your current annual income:'))

    y = ret - age

    hc = present_value_of_annuity(rr,y, ci)


    print 'You have '+str(y)+' remaining working years with an income of ' + dollar_format(ci) + ' per year.'
    print 'The present value of your human capital is about ' + dollar_format(hc)

    fa = int(input('Enter the value of your financial assets:'))

    con = annuity_payment(rr,(100-age),hc)
    #issue with con or with annuity payment function
    save = ci-con

    print 'Your economic net worth is:' + dollar_format(hc+fa)

    print 'Your sustainable standard of living is about ' + dollar_format(con)+ 'per year.'
    print 'To achieve this standard of living to age 100, you must save '+dollar_format(save)+' per year.'





if __name__ == '__main__':
    
    life_cycle_model()