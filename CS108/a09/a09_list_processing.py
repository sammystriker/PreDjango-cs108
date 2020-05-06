def my_sum(values):
    s = 0
    for i in values:
        s+=i
    return s
        
def my_max(values):
    m = values[1]
    for i in values:
        if i>m:
            m=i
    return m

def powers(base, n):
    r = []
    for i in range(n):
        r+=[(base**i)]
    return r

def get_uniques(items):
    r = []
    for x in items:
        if x not in r:
            r.append(x)
    return r

if __name__ == '__main__':
     values = [4, 7, 9, 2, 8, 5, 1, 6]
     words = ['to', 'be', 'or', 'not', 'to', 'be']
     print(get_uniques(words))

#code complete