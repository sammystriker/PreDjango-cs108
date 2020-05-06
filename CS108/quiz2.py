def upper_case(s):
    rs = ''
    for x in s:
        asc = ord(x)
        if (asc>96) and (asc<124):    #making sure the character is a lower case letter
            rs+=(chr(asc-32))         #adding adjusted character to new string 
        
        else:
            rs+=x                     #if character is not a lower case letter, add anyways
    return rs

#########################################################################################################

def outer_chars(s, n):
    rs = ''
    for i in range(n):
        rs+=s[i]                     # adds outer left chars 
    
    x = (s.__len__() - n)            # math for start point of next loop

    for i in range(n):
        rs+=s[x+i]                   # adds outer right chars 

    return rs

#########################################################################################################

def f_range(start, stop, step):
    r= [float(start)]

    ln = float(start)                #sets variable for last number added

    while ln != stop:                #while the last number is not the stop
        
        if ln+step == stop:          #if the next step is the stop, break the loop
            break
        else:
            r.append(ln+step)        #adds next step to list
            ln+=step                 #adjusts last number

    return r
        


#########################################################################################################

def count_vowels(s):
    vowels= {'a':0,'e':0,'i':0,'o':0,'u':0}       #create vowel dict

    for ch in s:
        if ch == 'a':        
            vowels['a']+=1                        #ammend dict if ch is 'a'
        
        if ch == 'e':
            vowels['e']+=1                        #ammend dict if ch is 'e'
        
        if ch == 'i':
            vowels['i']+=1                        #ammend dict if ch is 'i'
        
        if ch == 'o':
            vowels['o']+=1                        #ammend dict if ch is 'o'
        
        if ch == 'u':
            vowels['u']+=1                        #ammend dict if ch is 'u'

    return vowels


if __name__ == "__main__":
    print(upper_case("Holy, Moly, guacamole!"))
    print(outer_chars("Hello World",3))
    d= count_vowels("a long time ago in a galaxy far far away")
    print(dict(d))
    print(f_range(2,4,0.5))