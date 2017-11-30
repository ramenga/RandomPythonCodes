def getSublists(L, n):
    '''
    This function returns a list of all possible sublists 
    in L of length n without skipping elements in L. 
    The sublists in the returned list should be ordered 
    in the way they appear in L, with those sublists 
    starting from a smaller index being at the front of the list.
    '''
    sublist=[]
    for i in range(len(L)-n+1):
        sublist.append([L[i]])
        for j in L[(i+1):(i+n)]:
            sublist[i].append(j)
        
    return sublist
    
def isRun(k):
    for i in range(len(k)-1):
        if k[i]>k[i+1]:
            return False
        
    return True
    
def longestRun(L):
    '''
    Returns longest run occuring in L
    '''
    length = len(L)
    sublist=[]
    while length > 0:
        sublist=getSublists(L,length)
        for alist in sublist:
            if isRun(alist):
                return len(alist)
        length -=1
        