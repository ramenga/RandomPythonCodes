def f(a,b):
    return a>b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect={}
    difference={}
    i=0
    j=0
    re=()
    for i in d1:
        for j in d2:
            if i==j:
                intersect[i]=f(d1[i],d2[j])
            #elif (i not in d2) and j<i:
                #difference[j]=d2[j]
            #elif (j not in d1) and i<j:
                #difference[i]=d1[i]
                #difference[j]=d2[j]
            difference[i]=d1[i]
            difference[j]=d2[j]
    for i in intersect:
        if i in difference:
            del difference[i]

        
                
    re=(intersect,difference,)
    return re

                