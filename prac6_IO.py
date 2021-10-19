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
#import the module agentframework6 we created
import agentframework6
#import csv to import and read csv file
import csv

#store txt file as list of lists called "environment"
#create an empty list an assign it to the label "environment"
environment = []
with open('in.txt', newline='') as f:
    #read csv file
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #for the row
    for row in reader:
        #create list called "rowlist"
        rowlist = []
        #for the value in row:
        for value in row:
            rowlist.append(value)
        #creates environment from values
        environment.append(rowlist)
#print the environment
print (environment)

#create a function to return distance between agents_row_a and agents_row_b
def distance_between(agents_row_a, agents_row_b):
    #return the pythagorean distance
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)
    
#creation of ten agents
#assign the value "10" to the label "num_of_agents"
num_of_agents = 10

#creation of number of iterations 
#assign the value "100" to the label "num_of_iterations"
num_of_iterations = 100

#create an empty list an assign it to the label "agents"
agents = [] 

#start timing execution of code from here:
start = time.time() 

#create the agents
#for the number of agents:
for i in range(num_of_agents):
    #assign value to agents (refer to agentframework6)
    #pass in environment
    agents.append(agentframework6.Agent(environment))

#move the agents
#modify to eat as well
#for the number of iterations:
for j in range(num_of_iterations):
    #for the number of agents
    for i in range(num_of_agents):
        #print to see what the agents are before the move
        print (i, "before move", agents[i].x, agents[i].y)
        #move the agents
        agents[i].move()
        #print to see what the agents are after the move
        print (i, "after move", agents[i].x, agents[i].y)
        #print to see what value is before eat
        print ("store before eat", agents[i].store)
        #eat agents
        agents[i].eat()
        #print to see what it is after eat
        #has removed 10 from the value which is added to the agent store
        print ("store after eat", agents[i].store)
 
#displaying our environment data showing it nibbled away
#create plot y and x axis in range (0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
#for the number of agents
for i in range(num_of_agents):
    #plot scatter plot
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#show scatterplot 
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
 
#assign the value "3" to x
x = 3
#dot opperator '.' accesses code inside object (agent)
#passing in environment to agent
a = agentframework6.Agent(environment)
#go to a (agentframework6.py), look inside and find the y variable inside it
print(a.y) 
#go to a (agentframework6.py), look inside and find the x variable inside it
print(a.x)
#prints values for y and x
print(a.y, a.x)
print(x)

#calling on move function (defined in agentframework6)
a.move()

#prints values for y and x
print(a.y, a.x)

#print agents
#prints from return string function in agentframework 6
for i in range (num_of_agents):
    print (agents[i])
    #output prints values for "x", "y" and "store"
    
#end timing code execution time from here
end = time.time()

#print the execution time 
print("time = " + str(end - start))