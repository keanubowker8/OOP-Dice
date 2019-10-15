# Perfectly normal dice
You’ve all seen dice before. A die (singular for dice) usually has 6 sides. Sometimes a Die can have a different number of sides. Eg you can get an 8 sided die, or a 20 sided die. Dice can be rolled, if you roll a 6 sided die then you will get an integer result between 1 and 6 inclusive (1,2,3,4,5 or 6). If you roll an 8 sided die then you will get an integer result between 1 and 8 inclusive ((1,2,3,4,5,6,7 or 8)

A die has a value (eg if 1 dot is showing then the value is 1). When a die is rolled then it’s value randomly changes. A six sided die has a 1⁄6 chance of landing on any of the sides.

Create a class called Die. It should have an attribute named sides. sides has to be an integer that is greater than 1. Give your class a function called roll. Roll should update an attribute named value.


``` // Python

die6 = Die(6)
die6.roll()

die20 = new Die(20)
die20.roll()

print(die6.value) // this would print a number between 1 and 6 inclusive
print(die20.value) // this would print a number between 1 and 20 inclusive 
```

# Weighted Dice
Please extend your program with the following functionality.

Sometimes when dice are manufactured or altered so they are less than perfectly fair. These are called weighted or loaded dice.

For example we might have a weighted 6 sided die with the following probabilities of hitting various values:

Value	Chance of landing on value
1	1⁄7
2	1⁄7
3	1⁄7
4	1⁄7
5	1⁄7
6	2⁄7
If we roll this die 700 times then cances are we’ll get 200 6s, and 100 of each of the other values.

Extend the constructor of your class so that it has an optional parameter called probabilities. This would be an array of integers. The length of the array should be equal to the number of sides. If probabilities is left blank then the constructed Die instance should be fair.


``` #Python

 #looking at the data from the table above. this is how we would costruct the weighted die

dieDodgy6 = Die(6,[1,1,1,1,1,2])

 #we can create a perfectly fair die like this

die6 = Die(6,[1,1,1,1,1,1])

 #this is equivalent to

die6 = Die(6)
```

If there are any negative numbers in the probabilities array then raise the error negative probabilities not allowed.
If the sum of the numbers in the probabilities array is less than 1 then raise the error probability sum must be greater than 0
If the values passed in are not integers thenraise the error only integer values allowed
Create a function on your Die class called setProbabilities. This should take in an array and update the Die instance accordingly.

Add a function to your Die class called setProbabilities. This function should take in an array of integers.

# Dice Factory
Dice are made in a factory. A factory can only make one kind of die. Eg there could be a factory that only makes 6 sided dice, and another factory that only makes 20 sided dice.

Create a DiceFactory class. It should have a method called makeDie(js) or make_die(python) that outputs a single fair die instance

eg:


``` //Python

factory20 = DiceFactory(20)
die20 = factory20.make_ie()
anotherDie20 = factory20.make_die() 
```
This is a very somplified verion of the factory design pattern. Design patterns are cool you guys. Basically the idea behind this one is that some classes are hard to construct:

sometimes it’s hard to decide what to construct
sometimes the constructor has a lot of parameters
sometimes the constructor parameters themselves are complicated to construct
A factory can be initialised to know how to construct a specific thing. Interacting with factory should be very simple.
