import math

def is_valid_month(month):
    if month<13:
        if month>0:
            return True
    else:
        return False

def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else: 
                return False
        else: 
            return True
    else: 
        return False

def is_valid_day_in_month(month, day, year):
    if is_valid_month==False:
        return False
    if month in (1,3,5,7,8,10,12):
        if day>0 and day<32:
            return True
        else: 
            return False
    if month in (4,6,9,11):
        if day>0 and day<31:
            return True
        else: 
            return False
    if month==2:
        if is_leap_year(year):
            if day>0 and day<30:
                return True
            else: 
                return False
        else:
            if day>0 and day<29:
                return True
            else: 
                return False
    else:
        return False

def get_month_name(month):
    if month==1:
        return 'January'
    if month==2:
        return 'February'
    if month==3:
        return 'March'
    if month==4:
        return 'April'
    if month==5:
        return 'May'
    if month==6:
        return 'June'
    if month==7:
        return 'July'
    if month==8:
        return 'August'
    if month==9:
        return 'September'
    if month==10:
        return 'October'
    if month==11:
        return 'November'
    if month==12:
        return 'December'
    else:
        return str(month)

def is_valid_date(month, day, year):
    date = str(month)+'/'+str(day)+'/'+str(year)
    if is_valid_day_in_month(month,day,year):
        print date+' is a valid date.'
        return True
    else:
        if is_valid_month(month)==False:
            print date+' is a not valid date, because '+get_month_name(month)+' is not a valid month.'
            return False
        else:
            print date+' is a not valid date, because '+str(day)+' is not a valid date for '+get_month_name(month)+' '+str(year)
            return False

if __name__ == "__main__":
    print is_valid_date(14,30,2008)