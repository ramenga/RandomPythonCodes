def fib(x):
    '''
    x is an integer>=0
    returns xth fibo number
    '''
    assert type(x)==int and x>=0 #check input number
    if x==0 or x==1:
        return 1
    else:
        #summing the previous two numbers in the series
        return fib(x-1) + fib(x-2) #recurring into a lot of smaller x fibos