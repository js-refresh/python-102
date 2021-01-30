# class examples
def introduce(first, last):
    print(f'Introducing {first}, of house {last}!')
introduce('Arya', 'Stark')

# Callbacks
def greet(name):
    print(f'Hello, {name}')

def depart(name):
    print(f'Goodbye, {name}')

def interactTwice(name, action):
    action(name)
    action(name)

interactTwice('Molly', greet)
interactTwice('Molly', depart)

# What is an object?
#     It's just a 'thing', bunch of data, plus, has methods for working with that data
#     also callee attributes, properties, or state 
# what's an example of an object? 
#     A cat has.... fur, lives, legs, claws, tail (i.e. these are objects)
# How is an object created? 
    # It is 'instantiated', it's an instance of an object
    # 'Class' is like a blueprint, different than 'objects'
    # Instantiate cat!, start with a class
class Cat:
    # Class attibute
    species = 'mammal'

    # Initialize / Instance Attribute
    def _init_(self, name, age):
        self.name = name
        self.age = age

gus = Cat('Gus', 8)
print(f'{self.name} is {self.age} years old.')
print('%s is %s years old' %(self.name, self.age))
# .format(gus.name, gus.age))
