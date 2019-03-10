import math

def abs_sign(a):
    if type(a) == int:
        if a >= 0:
            return(a)
        else:
            return(-a)


def abs_square(a):
    if type(a) == int:
        return(math.sqrt(math.pow(a, 2)))


test = "hello"
test.isdigit()