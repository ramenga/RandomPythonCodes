print"Please think of a number between 0 and 100!"
low=0
high=100
mid=(high+low)/2
inp=''
while True:
    print("Is your secret number "+str(mid)+"?")
    inp=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if inp=='c':
        break
    elif inp == 'h':
        high=mid
    elif inp=='l':
        low=mid
    else:
        print"Sorry, I did not understand your input."
    mid=(high+low)/2
print"Game over. ",
print("Your secret number was: "+str(mid))
