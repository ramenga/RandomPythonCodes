class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        temp = super(ArrogantProfessor,self).say(stuff)
        splited = temp.split('I believe')
        return temp#splited[0] +'It is obvious'+splited[1]
        
    def lecture(self,stuff):
        temp = super(ArrogantProfessor,self).lecture(stuff)
        splited = temp.split('I believe')
        return 'It is obvious'+splited[1]
        
        
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')