# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:31:11 2021

@author: Christie
"""

#import random module - for random number generation
import random
    
#assign the value "50" to the coordinates "yO" and "x0"
y0 = 50
x0 = 50

#print the values for "y0" and "x0"
#shows "y0 = 50" and "x0 = 50" in output
print ("y0 = ", y0)
print ("x0 = ", x0)

#assign the label "random_number" to a random number
#random number generated by using "random.random()"
random_number = random.random()
#print the value of "random_number"
print ("random number = ", random_number)

#conditional statement for y value
#if random_number is less than 0.5 then:
if random_number < 0.5: 
    #add "1" to y0's value
    y0 = y0 + 1
#else / if random_number is not less than 0.5 then:
else:
    #subtract "1" from y0's value
    y0 = y0 - 1 


#Repeating for x
#assign the label "random_number" to a random number
#random number generated by using "random.random()"
random_number = random.random()
#print the value of "random_number"
print ("random number = ", random_number)

#if random_number is less than 0.5 then:
if random_number < 0.5:
    #add "1" to x0's value
    x0 = x0 + 1
#else / if random_number is not less than 0.5 then:
else:
    #subrtact "1" from x0's value
    x0 = x0 - 1
    
#print the new values for "y0" and "x0"
print ("y0 first move = ", y0)
print ("x0 first move = ", x0)


#copy code to move "y0" and "x0" a second time
random_number = random.random()
print (random_number)

if random_number < 0.5: 
    y0 = y0 + 1
else:
    y0 = y0 - 1 
    

if random_number < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
#print the new values for "y0" and "x0"
print ("y0 second move = ", y0)
print ("x0 second move = ", x0)


#creating a second set of coordinates "y1" and "x1" for a second agent 
#assign the value "50" to coordinates "y1" and "x1"
y1 = 50
x1 = 50

#print the values for "y1" and "x1"
#shows "y1 = 50" and "x1 = 50" in output
print ("y1 = ", y1)
print ("x1 = ", x1)


#assign the label "random_number" to a random number
#random number generated by using "random.random()"
random_number = random.random()
#print the value of "random_number"
print ("random number = ", random_number)

#conditional statement for y value
#if random_number is less than 0.5 then:
if random_number < 0.5: 
    #add "1" to y1's value
    y1 = y1 + 1
#else / if random_number is not less than 0.5 then:
else:
    #subtract "1" from y1's value
    y1 = y1 - 1 
    
    
#Repeating for x
#assign the label "random_number" to a random number
#random number generated by using "random.random()"
random_number = random.random()
#print the value of "random_number"
print ("random number = ", random_number)

#if random_number is less than 0.5 then:
if random_number < 0.5:
    #add "1" to x1's value
    x1 = x1 + 1
#else / if random_number is not less than 0.5 then:
else:
    #subtract "1" from x1's value
    x1 = x1 - 1
    
#print the new values for "y1" and "x1"
print ("y1 first move = ", y0)
print ("x1 first move = ", x0)


#calculate the pythagorean distance
#assign the label "distance" to the equation:
#(distance between y0 and y1)squared, plus
#the (distance between x0 and x1) squared
#all square rooted 
distance = (((y0-y1)**2) + ((x0-x1)**2))**0.5

#print the value for "distance"
print ("pythagorean distance = ", distance)

#Testing the code is correct (answer should be 5 if code is correct)
x0 = 0
y0 = 0
y1 = 4
x1 = 3

distance = (((y0-y1)**2) + ((x0-x1)**2))**0.5

#print the value for "distance"
print ("pythagorean distance test = ", distance)
#shows "5" in output