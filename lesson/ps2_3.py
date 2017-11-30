balance = 9876546 
annualInterestRate = 0.18
#above given
monthlyInterestRate = annualInterestRate / 12

lower = balance / 12
upper = (balance * (1 + monthlyInterestRate)**12) / 12.0
mid = (lower + upper)/2
balance2 = balance 
epsilon = 0.10  #acceptance

while (balance2 >= epsilon): #will break when balance2 is +ve but less than epsilon

    mid = (lower + upper)/2
    for i in range (1,13):
        unpaid = balance2 - mid
        balance2 = unpaid+(annualInterestRate/12*unpaid)
    
    print"balance2="+str(balance2)
    if (balance2 < 0): #you paid too much: bal is -ve
        upper = mid    #go lower
        balance2 = balance  # reset

    elif (balance2 > epsilon): #you paid too less: bal is +ve more than epsilon
        lower = mid         #go higher
        balance2 = balance  # reset
        

print "Lowest Payment: "+str(round(mid,2))