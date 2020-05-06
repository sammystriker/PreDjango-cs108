def shift_char(c, n):
    x = ord(c)
    # returns not a letter
    if (x>122 or x<65):
        return c
   
    #capital letter
    if x<=90:
        sc = x+n
        if sc>90:
            sc-=26
        return chr(sc)
    
    #lower case letter
    else:
        sc = x+n
        if sc>122:
            sc-=26
        return chr(sc)
    
def cipher(plaintext, n):
    ciphertext= ""
    for i in plaintext:
        nl = shift_char(i,n)
        ciphertext+= nl
    return ciphertext

def codebreaker(ciphertext):
    for i in range(26):
        print("Code "+str(i)+" means "+cipher(ciphertext,i))

if __name__ == '__main__':
     print(codebreaker("pxevhfx mh max ftvabgx"))

#code complete