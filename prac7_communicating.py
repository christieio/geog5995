# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:23:48 2021

@author: Christie
"""

#import matplotlib.pyplot to create visualisations (plot)
import matplotlib.pyplot
#import operator module to access efficient functions
import operator
#import random module to access random functions
import random
#to time how long a set of code takes to run (execution time)
#time takes longer the higher number of agents you have
import time 
#import the module agentframework7 we created
import agentframework7
#import csv to import and read csv file
import csv

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)

#start timing execution of code from here:
start = time.time() 

#stores txt file as list of list called environment
environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            #print(value)
            rowlist.append(value)
        environment.append(rowlist)

#print environment 
print (environment)

#define function called "distance_between" 
#returns pythagorean distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
         ((agents_row_a.y - agents_row_b.y)**2))**0.5 

#creation of ten agents
#assign the value "10" to the label "num_of_agents"
num_of_agents = 10

#creation of number of iterations 
#assign the value "3" to the label "num_of_iterations"
num_of_iterations = 3

#creation of neighbourhood
#attach value of "20" to label "neighbourhood"
neighbourhood = 20

#create an empty list an assign it to the label "agents"
agents = []

#create the agents
#for the number of agents
for i in range(num_of_agents):
    #assign value to agents (refer to agentframework7)
    #pass in agents id "i"
    #pass in agents "agents"
    #pass in environment "environment"
    agents.append(agentframework7.Agent(i, agents, environment))

#move the agents 
#modify to eat as well
#for the number of iterations
for j in range(num_of_iterations):
    #print after each iteration
    print ("iteration", j)
    #shuffle at end of each iteration
    #call on random function and then pass in the list (agents)
    random.shuffle(agents)
    #for the number of agents
    for i in range(num_of_agents):
        #print agents
        print (agents[i])
        #print to see what the agents are before the move
        print (i, "before move", agents[i].x, agents[i].y)
        #move the agents
        #refer to move function in agentframework7
        agents[i].move()
        #print to see what the agents are after the move
        print (i, "after move", agents[i].x, agents[i].y)
        
        #print to see what it is before eat
        print ("store before eat", agents[i].store)
        #eat agents
        agents[i].eat()
        #print to see what it is after eat
        #has removed 10 from the value which is added to the agent store
        print ("store after eat", agents[i].store)
    #for the number of agents
    for i in range(num_of_agents):
        #share with neighbourhoods
        agents[i].share_with_neighbours(neighbourhood)

#displaying our environment data showing it nibbled away
#create plot y and x axis in range (0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
#for the number of agents
for i in range(num_of_agents):
    #plot scatter plot
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#show plot
matplotlib.pyplot.show()
       
#to test whether the txt file has worked 
#if worked we should see a raster graph
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
#raster graph shown so code has worked successfully

#create a plot in the range (0, 99) y and x axis
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
#for the number of agents
for i in range(num_of_agents):
    #scatter the agents
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#show scatter plot
matplotlib.pyplot.show()

#returning the pythagorean distance
for agents_row_a in agents:
    for agents_row_b in agents:
        #return the pythagorean distance
        distance = distance_between(agents_row_a, agents_row_b)
        
x = 3
#dot opperator '.' accesses code inside object (agent)
#passing in agent id "i"
#passing in agents "agents" 
#passing in environment "environment" to agent 
a = agentframework7.Agent(i, agents, environment)
#go to a (agentframework7.py), look inside and find the y variable inside it
print(a.y) 
#go to a (agentframework7.py), look inside and find the x variable inside it
print(a.x)
#prints values for y and x
print(a.y, a.x)
print(x)

#calling on move function (defined in agentframework7)
a.move()
#print coordinates
print(a.y, a.x)

#print agents
#print final agents to make it clear in output
print ("final agents")
#prints from return string function in agentframework7
for i in range (num_of_agents):
    #print agents
    print (agents[i])
    #prints values for "id", "x", "y" and "store"
    
#end timing code execution time from here
end = time.time()

#print the execution time 
print("time = " + str(end - start))

# =============================================================================
# output
# # final agents
# # id = 2, x = 32, y = 64, store30.0
# # id = 3, x = 65, y = 52, store30
# # id = 4, x = 39, y = 60, store30.0
# # id = 9, x = 13, y = 76, store30.0
# # id = 6, x = 28, y = 63, store30.0
# # id = 7, x = 14, y = 33, store30
# # id = 0, x = 46, y = 98, store30
# # id = 1, x = 54, y = 2, store30
# # id = 8, x = 20, y = 93, store30.0
# # id = 5, x = 46, y = 71, store30.0
# 
# =============================================================================
