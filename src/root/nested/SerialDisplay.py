'''
Created on Mar 11, 2017

@author: David
'''
import serial
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
fig, ax = plt.subplots()
plt.title('Real-time Acceleration')
ln, =ax.plot([],[],'r-',animated = True)
plt.ion()

print("Entering drawing")

def update(frame):
   
    temp = ser.readline() #Read input
    temp = temp.split("\t") #split up tabs
    xVal.append(int(temp[1]))
    yVal.append(int(temp[2]))
    zVal.append(int(temp[3]))
    t.append(len(zVal)) #Add to "time" or x-axis
    
    ln.set_data(t,zVal)
    
    #Allow axes to resize automatically
    ax.relim()
    ax.autoscale_view()
    
    return ln


ani = animation.FuncAnimation(fig,update, interval = 20)
plt.show()