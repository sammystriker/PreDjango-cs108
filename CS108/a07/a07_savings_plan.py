def  print_monthly_savings_accumulation(rm, amount_saved, initial_balance = 0):
    bal = initial_balance
    # interest = balance * monthly interest rate.
    print("Month   Interest        Amount          Balance")
    for i in range(12):
        mon_int_earn = bal*rm
        bal+=amount_saved
        bal+=mon_int_earn
        print("   "+str(i)+"   $"+str(round(mon_int_earn,2))+"   $"+str(round(amount_saved,2))+"    $"+str(round(bal,2)))
    
    tot_am_sav = amount_saved*12
    print
    print("Total amount saved:    $   "+str(round(tot_am_sav,2)))
    print("Total interest earned: $   "+str(round(bal-tot_am_sav,2)))
    print("End of year balance:   $   "+str(round(bal,2)))
    
    return bal

def interactive_savings_plan():
    sg = int(input("Enter your savings goal in dollars: "))
    rr = int(input("Enter the expected annual rate of return (i.e. 0.03): "))
    y  = int(input("Enter time until goal in years: "))

    top = sg*rr
    mon = y*12
    yes = rr+1
    bot = yes**mon

    sav_am =top/(bot-1)

    # some arithmatic problem giving bottom a 0 which is causing error

    print("To reach your goal in "+str(y)+" years, you will need to save $"+str(round(sav_am,2))+" per month.")
    print 
    print

    bal = 0

    for i in range(y):
        print("Summary of year "+str(i))
        bal = print_monthly_savings_accumulation((rr/12),sav_am,bal)
        

if __name__ == '__main__':
    
    interactive_savings_plan()



