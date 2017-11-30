def printMove(fr,to):
    '''
    +just printing the move
    +carry on XO Pressly
    '''
    print('move from '+str(fr)+' to '+str(to))
    
def Towers(n,fr,to,spare):
    '''
    The base case is the move case, recursive
    +becoming things, to move is to become
    '''
    if n==1: #base case, when tower is of size 1
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to) #iterates into whole lot of smaller moves
        Towers(1,fr,to,spare) #actually doesnt' do much other than print move
        Towers(n-1,spare,to,fr)