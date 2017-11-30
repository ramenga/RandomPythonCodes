x = 23
epsilon = 0.05
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    print("inWhile guess="+str(guess))
    print("inWhile (guess**2-x)="+str(guess**2-x))
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)