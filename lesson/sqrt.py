x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x: #isnt so useful this condition
    print("inWhile guess="+str(guess))
    if abs(guess**2 -x) >= epsilon:
        print("inIF guess^2-x="+str(guess**2 -x))
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)