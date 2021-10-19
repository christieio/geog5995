# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:24:35 2021

@author: Christie
"""
#import random module - for random number generation
import random

#create a new class "Agent"
class Agent(): 
    #construction function __init__
    #self stores variables inside the object ()
    #ataches function to collection of code (self)
    def __init__ (self):
        #set up variables so x and y is a random number
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.store = 0
        
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
