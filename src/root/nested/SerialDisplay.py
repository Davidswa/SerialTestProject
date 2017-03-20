'''
Created on Mar 11, 2017

@author: David
'''
import serial
import matplotlib.pyplot as plt
from collections import deque

#Initialize variables
xVal = []
yVal = []
zVal = []
#t = []
d = deque([],maxlen=5000)
t = deque([],maxlen=5000)

#Setup Serial here
ser = serial.Serial('COM8',38400)
ser.flushInput() #prevents old data from screwing up the program

#Dump first three lines of header
for x in range(0,3):
    print(ser.readline())

#Setup plot
fig, ax = plt.subplots()
plt.title('Real-time Acceleration')
plt.ion()
ln, = ax.plot(t,zVal,'r-')
plt.show()

print("Entering drawing")

def update(temp):
   
    temp = temp.split("\t") #split up tabs
    xVal.append(int(temp[1]))
    yVal.append(int(temp[2]))
    zVal.append(int(temp[3]))
    #t.append(len(zVal)) #Add to "time" or x-axis
    
    d.append(int(temp[3]))
    t.append(range(0,len(zVal)))
    
    ln.set_data(t,zVal)
    print ln.get_xdata()
    return ln

while True:
    while ser.in_waiting == 0: #wait for incoming data
        pass
    datIn = update(ser.readline())
    
    fig.canvas.draw()
    ax.relim()
    ax.autoscale_view()
    #plt.show(block=False)
    
ser.close()