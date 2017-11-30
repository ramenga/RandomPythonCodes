balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#above given
monthlyInterest=annualInterestRate/12.0
month=1
unpaid=0
totalpaid=0
for month in range(1,13):
    print("Month: "+str(month))
    minMonthlyPay=balance*monthlyPaymentRate
    minMonthlyPay=round(minMonthlyPay,2)
    totalpaid+=minMonthlyPay
    print("Minimum monthly payment: "+str(minMonthlyPay))
    unpaid=balance-minMonthlyPay
    balance=(unpaid+(monthlyInterest*unpaid))
    balance=round(balance,2)
    print("Remaining balance: "+str(balance))
print("Total paid: "+str(totalpaid))
print("Remaining balance: "+str(balance))
    
    