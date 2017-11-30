def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    keys = d.keys()
    values = d.values()
    done=[]
    invert = dict()
    for i in range(len(values)):
        if values[i] not in done:
            invert[values[i]]=[keys[i]]
        else:
            invert[values[i]].append(keys[i])
        done.append(values[i])
    for val in invert:
        invert[val].sort()
            
        
    return invert