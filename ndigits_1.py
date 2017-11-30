def ndigits(x):
    """
    input: interger number
    output: digits of the number (base 10)
    recursive function
    """
    assert type(x)==int
    #the funtion does not work with a not integer number
    xabs = abs(x)
    if xabs/10==0:
        return 1
    else:
        return 1 + ndigits(xabs/10)

print ndigits(100)