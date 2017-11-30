class Queue(object):
    def __init__(self):
        self.vals=[]
        
    def insert(self,x):
        #self.x=x
        self.vals.append(x)
    
    def remove(self):
        try:
            a=x[0]
            self.vals.remove(a)
            return a
        except ValueError:
            raise ValueError()