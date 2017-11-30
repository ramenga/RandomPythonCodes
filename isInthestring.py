def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    first=0
    last=len(aStr)
    mid=(first+last)/2
    
    #base cases
    if aStr=='': 
        return False
    elif (len(aStr)<=1 and aStr[mid]==char) or aStr[mid]==char: 
        return True
    elif len(aStr)<=1 and aStr[mid]!=char:
        return False
        
    #recursive cases
    if char>aStr[mid]:
        return isIn(char,aStr[mid:])
    elif char<aStr[mid]:
        return isIn(char,aStr[0:mid])
        
    
        
    