# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:24:35 2021

@author: Christie
"""

#import random module - for random number generation
import random

#create "Agent" class
class Agent(): 
    #construction function __init__
    #self stores variables inside the object ()
    #ataches function to collection of code (self)
    #passing environment into each agent, storing it as an instance variable
    def __init__ (self, environment):
        #here we set up variables so x and y is a random no
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        #create store
        self.store = 0
        
    #define new string function to return values for x y and store
    def __str__ (self):
        #returning x, y and store as a string
        #use of string so it isn't recognised as a number
        return "x= " + str(self.x) \
            + ", y= " + str(self.y) \
                + ", store= " + str(self.store)
        
    #define a function called "move" in order to move the agents
    def move (self):
        #if random number is less than 5 then:
        if random.random() < 0.5:
            #add "1" to y 
            self.y = (self.y + 1) % 100
        #or else
        else:
        #or else, subtract "1" from y
            self.y = (self.y - 1) % 100

        #if random number is less than 5 then:
        if random.random() < 0.5:
            #add "1" to x
            self.x = (self.x + 1) % 100
        #or else
        else:
            #subtract "1" from x
            self.x = (self.x - 1) % 100


#defining a new function called eat
#finds out from environment if the value is greater than ten then it takes 
#ten from the value and adds it to the agent store
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10