import random
random.seed(9001)
class Die():
        
    value = 0
    
    def __init__(self,sides, probabilities=None):
        self.sides = sides
        self.probabilities = probabilities
 
    
    
    def setProbabilities(self):
        if self.probabilities==None:
            self.probabilities = [1 for i in range(self.sides)]    
        if type(self.probabilities) == list:
            assert len(self.probabilities) == self.sides
            for number in self.probabilities:
                if number < 0:
                    raise ValueError('negative probabilities not allowed')
            if sum(self.probabilities)<1:
                raise ValueError('probability sum must be greater than 0')
        numbers = []
        lst = self.probabilities
        for i in range(1,self.sides+1): 
            numbers.append(str(i))
        new = [numbers*lst for numbers,lst in zip(numbers,lst)]
        newlst = [b for i in new for b in i]
        return newlst
    
    
           
        
    def roll(self):
        lst = self.setProbabilities()    
        random_number = random.choice(lst)
        self.value = random_number   
        
            
        
die6 =  Die(6)
die6.roll()
print(die6.value)



class DiceFactory():
    value = 0
    
    def __init__(self,sides):
        self.sides = sides
        
        
    def make_die(self):
         self.value = random.randrange(1, self.sides+1)
         print(self.value)
         return self.value



factory20 = DiceFactory(20)
a = factory20.make_die()         