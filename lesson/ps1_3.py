def item_order(order):
    '''
    Takes as input a string named order. 
    String contains only words for the items the customer can order separated by one space. 
    Function returns a string that counts the number of each item
    Consolidates them in the following order: 
    salad:[# salad] hamburger:[# hambruger] water:[# water]

    If an order does not contain an item, then the count for that item is 0.
    '''
    salad=order.count('salad')
    hamburger=order.count('hamburger')
    water=order.count('water')
    urgent="salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return urgent
    
