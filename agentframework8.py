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
    #pass in "i" for the agents id
    #passing environment into each agent, storing it as an instance variable
    def __init__ (self, i, agents, environment):
        #here we set up variables so x and y is a random no
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        #create and store agents
        self.agents = agents
        self.environment = environment
        #create store
        self.store = 0
        #create and store "i" for agents id
        self.i = i
        
    #add new string function to return values for x y and store
    def __str__ (self):
        #returning x, y and store as a string
        #use of string as it needs to not recognise it as a number
        return "id = " + str(self.i) \
            + ", x = " + str(self.x) \
                + ", y = " + str(self.y) \
                    + ", store" + str(self.store)
        
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
            
    #defining a new function called distance_between
    def distance_between (self, b):
        #returns distance between (self x coordinate and b's x coordinate)**2
        #plus the distance between (self y coordinate and b's y cooridinate)**2
        #all square rooted
        return (((self.x - b.x)**2) + ((self.y - b.y)**2))**0.5
            
            
    #defining a new function called share_with_neighbours
    def share_with_neighbours (self, neighbourhood):
        #print neighbourhod
        print ("neighbourhood", neighbourhood)
        
        #loop through the agents in self.agents
        for i in range(len(self.agents)):
            
            # Calculate the distance between self and the current other agent:
            #uisng agents[i] as index to loop through all agents
            #ensure it's self. to avoid 'undefined' error message
            distance = self.distance_between(self.agents[i])
        #print distance 
        #print("distance", distance)
        #if distance is less than or equal to the neighbourhood (20)
        if distance < neighbourhood:
            #print distance
            print ("distance", distance)
            #sum self.store and agent.store
            #total used for sum as sum has other usage in python
            total = self.store + self.agents[i].store
            #divide sum by two to calculate average.
            average = total / 2
            #self.store = average
            self.store = average
            #agent.store = average
            self.agents[i].store = average

