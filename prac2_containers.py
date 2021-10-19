# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:31:11 2021

@author: Christie
"""

#import matplotlib.pyplot to create visualisations (plot)
import matplotlib.pyplot
#import operator module to access efficient functions
import operator
#import random module to access random functions
import random

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)

#create an empty list an assign it to the label "agents"
agents = [] 

#assignin a random number between 0 and 99 to agents[0][0] and agents[0][1]
agents.append([random.randint(0,99), random.randint(0,99)])

#print the value for the agents (coordinates y and x)
print ("agents", agents) 
 
#move the y coordinate

#assign the label "random_number" to a random number
#random number generated by using "random.random()"
random_number = random.random()
#print the value of "random_number"
print ("random number", random_number)

#conditional statement for agents[0][0]
#corresponds to the y coordinate
#if random number is less than 0.5 then:
if random_number < 0.5: 
    #add "1" to the value of agents[0][0]
    agents[0][0] = agents[0][0] + 1
#if random number is not less than 0.5 then:
else:
    #subtract "1" from the value of agents[0][0]
    agents[0][0] = agents[0][0] - 1 


#repeat to move the x coordinate

#assign the label "random_number" to a random number
#random number generated by using "random.random()"
random_number = random.random()
#print the value of "random_number"
print ("random number", random_number)

#conditional statement for agents[0][1]
#corresponds to the x coordinate 
#if random number is less than 0.5 then:
if random_number < 0.5:
    #add "1" to the value of agents [0][1]
    agents[0][1] = agents[0][1] + 1
#if random number is not less than 0.5 then:
else:
    #subtract "1" from the value of agents[0][1]
    agents[0][1] = agents[0][1] - 1
    
#print the new values for agents[0][0] and agents[0][1]
print ("agents first move = ", agents[0][0], agents[0][1])

#moving the agents a second time by copying code
#moving agents[0][0] ~ corresponds to y coordinates
random_number = random.random()
print ("random number", random_number)

if random_number < 0.5: 
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1 
    
#moving agents[0][1] ~ corresponds to x coordinates
random_number = random.random()
print ("random number", random_number)

if random_number < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
    
#print the new values for agents[0][0] and agents[0][1] after a second move
print ("agents second move = ", agents[0][0], agents[0][1])

#create a second set of coordinates for a second agent

#assignin a random number between 0 and 99 to agents[1][0] and agents[1][1]
agents.append([random.randint(0,99), random.randint(0,99)])
#print coordinates for agents 
print ("agents", agents) 

#move the y coordinate of second agent

#again generating a random number
random_number = random.random()
#print the value of "random_number"
print ("random number", random_number)

#conditional statement for agents[1][0]
#corresponds to the y coordinate
#if random number is less than 0.5 then:
if random_number < 0.5: 
    #add "1" to the value of agents[1][0]
    agents[1][0] = agents[1][0] + 1
#if random number is not less than 0.5 then:
else:
    #subtract "1" from the value of agents[1][0]
    agents[1][0] = agents[1][0] - 1 

#repeat to move the x coodinate of second agent

#again generating a random number
random_number = random.random()
#print the value of "random_number"
print ("random number", random_number)

#conditional statement for agents[1][1]
#corresponds to the x coordinate
#if random number is less than 0.5 then:
if random_number < 0.5:
    #add "1" to the value of agents[1][1]
    agents[1][1] = agents[1][1] + 1
#if random number is not less than 0.5 then:
else:
    #subtract "1" from the value of agents[1][1]
    agents[1][1] = agents[1][1] - 1
    
#print the new values for agents[1][0] and agents[1][1]
print ("second agent first move", agents) 

#moving the agents a second time by copying code
#moving agents[1][0] ~ corresponds to y coordinates

random_number = random.random()
print (random_number)

if random_number < 0.5: 
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1 
    
#moving agents[1][1] ~ corresponds to x coordinates

random_number = random.random()
print ("random number", random_number)

if random_number < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
    
#print the new values for agents[1][0] and agents[1][1] after a second move
print ("second agent second move", agents) 




#finding out which agent is furthest east

#print the agent with the maximum value
print ("max agents", max(agents))

print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(99, 47, color='red')
matplotlib.pyplot.show()


#calculate the pythagorean distance
#assign the label "distance" to the equation:
#(distance between agents[0][0] and agents[1][0])squared, plus
#the (distance between agents[0][1] and agents[1][1]) squared
#all square rooted 
distance = (((agents[0][0]) - (agents[1][0])**2) + ((agents[0][1])\
                                                    - (agents[1][1])**2))**0.5

#print the value for "distance"
print ("pythagorean distance = ", distance)
