def my_min(a,b):
    if a<b:
        return a
    else:
        return b

def find_min(a,b,c):
    if a<=b:
        if a<=c:
            return a
        else:
            return c
    else:
        if b<=c:
            return b
        else:
            return c







if __name__ == '__main__':
    print('my_min(1,2)', my_min(1,2))
    print('my_min(2,1)', my_min(2,1))
    print str(find_min(3,8,4))
