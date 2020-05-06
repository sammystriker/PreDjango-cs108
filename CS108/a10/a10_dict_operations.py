def print_dict(d):
    nd = sorted(d)
    for key in nd:
        print key,d[key]



if __name__ == '__main__':
     d1 = {'BU': 5, 'BC':3, 'Harvard':4, 'Northeastern':1} # alpha keys
     print_dict(d1)