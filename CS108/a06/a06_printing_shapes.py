def print_rect(ch,width,height):
    for i in range(height):
        print ch*width

def print_upper_left_triangle(ch,height):
    for i in range(height):
        print ch*(height-i)

def print_upper_right_triangle(ch, height): #broken
    for i in range(height):
        print (' '*i)+(ch*(height-i))
    
def print_lower_left_triangle(ch, height):
    for i in range(height+1):
        print (ch*i)+(' '*(height-i))

def print_lower_right_triangle(ch, height):
    for i in range(height+1):
        print (' '*(height-i))+(ch*i)

def print_pyramid(ch, height):
    for i in range(height):
        print ' '*(height-i-1) + ch*(2*i+1)

def print_diamond(ch, height):
    for i in range(height):
        print ' '*(height-i-1) + ch*(2*i+1)
    for j in reversed(range(height)):
        print ' '*(height-j-1) + ch*(2*j+1)


if __name__ == '__main__':
    print_rect('*', 7, 5)
    print
    print_upper_left_triangle('*',7)
    print
    print_upper_right_triangle('*',4)
    print
    print_lower_left_triangle('*',5)
    print
    print_pyramid('*',4)
    print
    print_diamond('*',4)

