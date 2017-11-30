def nfruits(fruitList,eatenFruits):
    '''
    This function takes in two arguments.  A non empty dictionary containing
    the characters and numbers representing the fruits and quantities available.
    It also takes the number of eaten fruits represented by characters and returns
    an int, indicating the maximum number of any kind of fruit left
    fruitList is non-empty dictionary
    eatenFruits is string
    '''
    
    ctr=0 #counter for the while loop
    typeOfFruit=''
    
    while ctr < len(eatenFruits):
    
        typeOfFruit=eatenFruits[ctr:ctr+1] # gets the next eaten fruit in the list
        fruitList[typeOfFruit]-=1 #update the fruitList by removing the consumed fruit
        ctr+=1
        
        if ctr==len(eatenFruits): #condition to check if its the last fruit in the list
            break
        #add 1 to all the other fruits
        for n in fruitList:
            if not n==typeOfFruit:
                fruitList[n]+=1
                
    result= max(fruitList, key=fruitList.get) # get the maximum fruit number
    return fruitList[result]