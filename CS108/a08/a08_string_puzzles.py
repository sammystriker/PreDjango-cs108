def reverse(s):
    l = len(s)
    r = s[-1:(-l-1):-1]
    return r

def every_other(s):
    l = len(s)
    return s[0:l:2]

def outside_chars(s, n):
    beg = s[:n]
    end = s[(-n-1):-1:1]
    return beg+end

def triple_outsides(s):
    tf = s[0]*2
    tl = s[-1]*2
    return tf+s+tl

def swap_halves(s):
    l = len(s)
    fh = s[0:(l/2)]
    lh = s[(l/2):l]
    return lh+fh

def slice_middle(s):
    l = len(s)
    return s[(l/4):-(l/4):1]

if __name__ == '__main__':
     print(slice_middle("welcome to the party"))
     
#code complete