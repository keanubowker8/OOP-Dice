import random
random.seed(9001)
class Die():
        
    value = 0
    
    def __init__(self,sides, probabilities=None):
        self.sides = sides
        if probabilities==None:
            probabilities = [1 for i in range(self.sides)]    
        if type(probabilities) == list:
            assert len(probabilities) == sides
            for number in probabilities:
                if number < 0:
                    raise ValueError('negative probabilities not allowed')
            if sum(probabilities)<1:
                raise ValueError('probability sum must be greater than 0')
        self.probabilities = probabilities
 
    
    
    def setProbabilities(self):
        numbers = []
        lst = self.probabilities
        for i in range(1,self.sides+1): 
            numbers.append(str(i))
        new = [numbers*lst for numbers,lst in zip(numbers,lst)]
        newlst = [b for i in new for b in i]
        #print(newlst)
        return newlst
    
    
           
        
    def roll(self):
        lst = self.setProbabilities()    
        random_number = random.choice(lst)
        self.value = random_number
    
# lst = setProbabilities()    
# random_word = random.choice(lst)
# print(random_word)    
        
            
        
die6 =  Die(6)
die6.roll()

# die20 =  Die(6,[1,1,2,1,5,2])
# die20.roll()

print(die6.value) # this would print a number between 1 and 6 inclusive
#print(die20.value) # this would print a number between 1 and 20 inclusive       