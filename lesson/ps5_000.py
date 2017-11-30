def modSwapSort(L): 
    """ L is a list on integers """
    count =0
    print "Original L: ", L
    
    for i in range(len(L)):
        count+=1
        for j in range(len(L)):
            count+=1
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L
    print "count:"+str(count)