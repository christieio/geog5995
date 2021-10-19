#importing all the modules needed for the code to run:
    
#import random module to access random functions
import random
import operator
#import tkinter for GUI programming
import tkinter
#import matplotlib to create visualisations (plot)
import matplotlib
#render backend associated with tkinter
matplotlib.use('TkAgg')
#matplotlib.pyplot imported to aid in the creation of the plot
import matplotlib.pyplot
#matplotlib.animation imported so there can be a live animation on the plot
import matplotlib.animation 
#import csv to import and read csv file
import csv
#import agentframework9 so we can communicate with code in this module
import agentframework9
#import requests and bs4 for webscraping
#import requests to send HTTP requests
import requests
#import beautiful soup to pull out data from HTML and XML files
import bs4

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)

#accessing webpage using requests function 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
#pulling out information from webpage and turn it into working python code
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

##imported code from model
#stores txt file as list of list called environment
environment = []
with open('in.txt', newline='') as f:
    #read csv file
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            #print(value)
            rowlist.append(value)
        environment.append(rowlist)
#print environment        
print (environment)


#defining a new function called distance_between to return distance between\
#agents_row_a and agents_row_b
def distance_between(agents_row_a, agents_row_b):
    #return result for pythagorean distance
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



#make the agents
#in the range of the number of agents:
for i in range(num_of_agents):
    #assign value to agents (refer to agentframework9)
    #pass in agents id "i"
    #pass in agents "agents"
    #pass in environment "environment"
    agents.append(agentframework9.Agent(i, agents, environment))


#define new function called run
def run():
    animation = matplotlib.animation.FuncAnimation\
        (fig, update, frames=gen_function, repeat=False)
    canvas.draw()
#add figure and assign its size
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#add y and x axes 
ax = fig.add_axes([0, 0, 1, 1])

#building the main window using root
root = tkinter.Tk()
#sets title as "Model"
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#creating a menu bar
menu_bar = tkinter.Menu(root)
root.config(menu = menu_bar)
model_menu = tkinter.Menu(menu_bar)
#label the menubar "Model"
menu_bar.add_cascade(label = "Model", menu = model_menu)
#add a command "run model" so when clicked model will run
#using run function defined higher up in code
model_menu.add_command(label = "Run model", command = run)

#define label "carry_on" as "true"
carry_on = True	
	
#define a new function called "update"
#pass in parameter "frame_number"
#allows frame number to be updated so we can see the model moving
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
        #on printing can see it has removed 10 from the value which it has\
            #added to the agent store
        print ("store after eat", agents[i].store)
    for i in range(num_of_agents):
        #share with neighbourhoods
        agents[i].share_with_neighbours(neighbourhood)
     
    #stopping condition
    #if random nummber is less than 0.01 then:
    if random.random() < 0.01:
        #stop
        carry_on = False
        #print "stopping condition" to see where this occurs
        print("stopping condition")
    
    #in the range of the number of agents
    for i in range(num_of_agents):
        #plot the points on top of environment
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i].x,agents[i].y)
        #in the output we see the defined number of agents plotted \
            #over the environment

#define a new function called "gen_function"
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        #return control and await next call
        yield a			
        a = a + 1

#show the plot
matplotlib.pyplot.show()

#print agents
#print final agents to make it clear in output
print ("final agents")
#prints from return string function in agentframework9
for i in range (num_of_agents):
    print (agents[i])

#sets the GUI waiting for events
tkinter.mainloop()


