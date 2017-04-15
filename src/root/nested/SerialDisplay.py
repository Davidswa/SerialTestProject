'''
Created on Mar 11, 2017

@author: David
'''
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#Initialize variables
xVal = []
yVal = []
zVal = []
t = []

#Setup Serial here
ser = serial.Serial('COM8',38400)
ser.flushInput() #prevents old data from screwing up the program

#Dump first three lines of header
for x in range(0,3):
    print(ser.readline())

#Setup plot
print("Starting figure setup\n")
fig, ax = plt.subplots()
line, = ax.plot(t, zVal)
ax.set_ylim(-65500,65500)
ax.set_xlim(0,1000)
plt.title('Real-time Acceleration')

print("Entering drawing")

def update(i,temp):
    print("Entered update\n")
    temp = temp.split("\t") #split up tabs
    xVal.append(int(temp[1]))
    yVal.append(int(temp[2]))
    zVal.append(int(temp[3]))

    t.append(len(zVal)) #Add to "time" or x-axis
    
    line.set_data(t, zVal)
    
    return line

def init():
    line.set_data(t, zVal)
    print("initialize complete\n")
    return line

def frameSource():
    print("frameSource called\n")
    return ser.readline()
    
ani = animation.FuncAnimation(fig, 
                              update,
                              init_func=init,
                              fargs=(frameSource), 
                              interval=0.01, 
                              blit=True)
plt.show()

ser.close()