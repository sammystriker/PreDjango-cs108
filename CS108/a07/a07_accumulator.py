def sum_of_range(start,stop,skip):
    s = 0 
    for i in range(start,stop,skip):
        s+=i
    return s

def replace(s, old_ch, new_ch):
    s=""
    for ch in s:
        if ch==old_ch:
            s+=new_ch
        else:
            s+=ch
    return s

def calculate_average():
    print("This program will compute the average of numerical observations.")
    print
    
    s = 0
    amount = int(input("How many observations do you have? "))
    
    for i in range(amount):
        num = int(input("Enter next value: "))
        s+= num
    
    ave= s/amount
    print("The average is "+str(ave))

if __name__ == '__main__':
    print('sum_of_range(1,5,1)', sum_of_range(1,5,1))
    print('sum_of_range(5,15,2)', sum_of_range(5,15,2))
    print(calculate_average())

# prints out a NONE at the end
#otherwise code complete