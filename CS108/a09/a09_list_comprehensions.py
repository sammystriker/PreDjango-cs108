def triple(values):
    new = []
    for i in values:
        new.append(i*3)
    return new

def get_powers(base, n):
    r = []
    for i in range(n):
        r+=[(base**i)]
    return r

def get_factors(n):
    r = []
    for i in range(n):
        if n%(i+1)==0:
            r.append(i+1)
    return r

def most_factors(numbers):
    mf = 0
    num = 0
    for i in numbers:
        amount = len(get_factors(i))
        if amount>mf:
            mf = amount
            num = i
    return num

#code complete


