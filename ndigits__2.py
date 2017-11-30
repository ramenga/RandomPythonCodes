def ndigits(x):
    '''
    x: An integer, either positive or negative
    return: the number of digits in inpuit x
    '''
    if x < 0:
        x = -x
    if x < 10:
        return 1
    else:
        return 1 + ndigits(x/10)