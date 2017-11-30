balance = 4773
annualInterestRate = 0.2
#above given
month=0
monthlyIntRate=annualInterestRate/12.0
payment=0.0
unpaid=0
balance2=balance
while(balance2>0):
    payment+=10.0
    balance2=balance
    for month in range(1,13):
        unpaid=balance2-payment
        balance2=unpaid+(unpaid*monthlyIntRate)
print("Lowest Payment: "+str(payment))
        

    