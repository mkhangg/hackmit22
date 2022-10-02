# Import neccessary libraries
from Control import *
from Ultrasonic import *

# Create control and ultrasensor objects
ctrol = Control()
sonic = Ultrasonic()

# File specifications
filePath = "/home/pi/robot/output.txt"
f = open(filePath, "r")

# Load data from text file
data = np.loadtxt(filePath)
data = int(data.item())

# Parameters for control
times = 1
angle = int(data/3) - 3
distance = int(sonic.getDistance())

# print(">> angle =", data)
print(">> distance =", distance)

# Move forward 20 based on y-coordinates
for i in range(times):
    data = ['CMD_MOVE', '1', '0', '20', '10', '0']
    ctrol.run(data)

# Move backward -20 based on y-coordinates
for i in range(times):
    data = ['CMD_MOVE', '1', '0', '-20', '10', '0']
    ctrol.run(data)

# Rotate based on angle of arrival of the sound 
for i in range(times):
    data = ['CMD_MOVE', '2', '0', '0', '10', f'{angle}']
    ctrol.run(data)

# Move toward the sound source
for i in range(times*5):
    data = ['CMD_MOVE', '1', '0', f'{distance}', '10', '0']
    ctrol.run(data)
