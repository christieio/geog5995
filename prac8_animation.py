#import matplotlib.pyplot to create visualisations (plot)
import matplotlib.pyplot
#matplotlib.animation imported so there can be a live animation on the plot
import matplotlib.animation 
#import operator module to access efficient functions
import operator
#import random module to access random functions
import random 
#import csv to import and read csv file
import csv
#import the module agentframework8 we created
import agentframework8

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)

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
    #assign value to agents (refer to agentframework8)
    #pass in agents id "i"
    #pass in agents "agents"
    #pass in environment "environment"
    agents.append(agentframework8.Agent(i, agents, environment))

#create a figure 
#show plot on figure
#create the size of the figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#add x and y axes to figure
ax = fig.add_axes([0, 0, 1, 1])

#define label "carry_on" as "true"
carry_on = True	
	
#define a function called "update"
#pass in perameter "frame_number"
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    #showing the environment on plot
    matplotlib.pyplot.imshow(environment)
    #setting the plot limit to between 0 and 99 for y and x
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)

    #print after each iteration
    print ("frame number", frame_number)
    #shuffle at end of each iteration
    #call on random function and then pass in the list (agents)
    #shuffle turned off for animation to make it clear what's happening
    #random.shuffle(agents)
    for i in range(num_of_agents):
        print (agents[i])
        #print to see what the agents are before the move
        print (i, "before move", agents[i].x, agents[i].y)
        #move the agents
        agents[i].move()
        #print to see what the agents are after the move
        print (i, "after move", agents[i].x, agents[i].y)
        
        #print to see what it is before eat
        print ("store before eat", agents[i].store)
        #eat agents
        agents[i].eat()
        #print to see what it is after eat
        #on printing we can see it has removed 10 from the value\
        #which is added to the agent store
        print ("store after eat", agents[i].store)
    #for the number of agents
    for i in range(num_of_agents):
        #share with neighbourhoods
        agents[i].share_with_neighbours(neighbourhood)
        
    #stopping condition 
    #if random number is less than 0.01 then:    
    if random.random() < 0.01:
        #don't carry on
        carry_on = False
        #print stopping condition to see where this occured
        print("stopping condition")
    
    #for the number of agents
    for i in range(num_of_agents):
        #plot points on top of environment
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i].x,agents[i].y)

#define function called "gen_function"
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        #return control and await next call
        yield a			
        a = a + 1


#create animation using defined functions above
#updates the frame so we can see a live animation
animation = matplotlib.animation.FuncAnimation\
    (fig, update, frames=gen_function, repeat=False)

#show plot
matplotlib.pyplot.show()

#print agents
#print final agents to make it clear in output
print ("final agents")
#prints from return string function in agentframework8
for i in range (num_of_agents):
    print (agents[i])
    
