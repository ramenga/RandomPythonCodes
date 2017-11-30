def genPrimes():
    P=[2]
    start=2
    isPrime=True
    yield start
    while True:
        start +=1
        isPrime=True
        for num in P:
            if (start%num)==0:
                isPrime=False
        if isPrime == True:
            P.append(start)
            yield start