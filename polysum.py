from math import* #import everything from math library

def polysum(n,s):
    '''
    A function that returns the sum of Area and Square of perimeter
    n-number of sides
    s-length of a side
    * Area: (0.25*n*s^2)/tan(pi/n)
    * Perimeter: length of the boundary of the polygon
    '''
    area=((0.25*n*s*s)/tan(pi/n)) #polygon area
    peri=n*s                      #perimeter
    sum=area+(peri**2)            #sum as specified
    return (round(sum,4))        #returns sum rounded to 4 decimal places
    