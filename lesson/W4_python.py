def nfruits(fruDic,fruStr):
    '''
    For example, if the initial quantities are {'A': 1, 'B': 2, 'C': 3} and the string pattern is 'AC' then
    'A' is consumed, updated values are {'A': 0, 'B': 2, 'C': 3}
    Python buys 'B' and 'C', updated values are {'A': 0, 'B': 3, 'C': 4}
    'C' is consumed, updated values are {'A': 0, 'B': 3, 'C': 3}
    '''
    done=0 #keeping check of iteration
    
    for i in fruStr: #for every element in fruit string
        if i in fruDic:
            done+=1 #increment iteration counter
            fruDic[i]-=1  #subtract the fruit eaten
            for j in fruDic:  #for every key in dictionary
                if j != i and done<len(fruStr):  #if fruit is not the last and not the one eaten currently
                    fruDic[j]+=1 #increment other fruits
                    
            
    return max(fruDic.values())  #return max value