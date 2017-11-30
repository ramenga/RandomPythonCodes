# -*- coding: utf-8 -*-
def ndigits(x):
    '''
    A function called “ndigits”.
    Takes an integer ‘x’ (either positive or negative) as an argument. 
    This function returns the number of digits in the integer x.
    This function is recursive.
    '''
    #checking for a negative number
    if x<0:
        x=abs(x) #performing on +ve version yiedls the same result
        
    if x==0: #checking for the last step or end of the recursion
        return 0 
    else:
        x=x/10 #shave off the last digit
        
        #this recursive return will add the count up from the end of recursion
        return 1+ndigits(x) 