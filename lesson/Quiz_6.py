def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    guy=[]
    for element in aList:
        #print "for",
        #print element
        if type(element)==list:
            #print "if",
            #print element
            guy += flatten(element)
        elif type(element)!=list:
            #print "eliif",
            #print element
            guy.append(element)
        
    return guy