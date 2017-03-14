'''
Created on Mar 11, 2017

@author: David
'''
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.tkagg import blit


#Initialize variables
xVal = []
yVal = []
zVal = []
t = []
data = [None]

#Setup Serial here
ser = serial.Serial('COM8',38400)

#Dump first three lines of header
for x in range(0,3):
    print(ser.readline())

#Setup plot
fig, ax = plt.subplots()
plt.title('Real-time Acceleration')
ln, = ax.plot(data)


print("Entering drawing")

def update(foo):
   
    temp = ser.readline()
    temp = temp.split("\t")
    xVal.append(int(temp[1]))
    yVal.append(int(temp[2]))
    zVal.append(int(temp[3]))
    
    ln.set_ydata(zVal)
    ln.set_xdata(t.append(foo))
    
    print len(zVal)
    print len(t)
    print("\n")
    
    return ln

 
ani = animation.FuncAnimation(fig,update,interval = 200, blit=False)
plt.show()