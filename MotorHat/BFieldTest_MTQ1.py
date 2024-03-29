from adafruit_motorkit import MotorKit
from time import sleep
import board
import csv

'''Test magnetorquers field strength using VN 200 10 cm away.
measured from end of MTQ holder to face of VN200 in X direction
setting | time duration (seconds)
0    | 10
ramp   1
5      10
ramp   1
0      10
ramp   1
-5     10
ramp   1
0      10 '''

c = open('magTestprograms.csv','w')

print('Start')

kit = MotorKit()

step = 1/10
xRange = int(1/step)

# 0V for 10 secs
kit.motor1.throttle = None
sleep(10)

# ramp 5V for 1 sec
for i in range(xRange):
    kit.motor1.throttle = (step*i)
    sleep(step)

# 5V for 10 sec
kit.motor1.throttle = 1
sleep(10)

# ramp 0V for 1 sec
for i in range(xRange):
    kit.motor1.throttle = 1 - (step*i)
    sleep(step)

# 0V for 10 secs
kit.motor1.throttle = 0
sleep(10)

# ramp to -5V for 1 sec
for i in range(xRange):
    kit.motor1.throttle = 0 - (step*i)
    sleep(step)

# -5V for 10 sec
kit.motor1.throttle = -1
sleep(10)

# ramp 0V for 1 sec
for i in range(xRange):
    kit.motor1.throttle = -1 + (step*i)
    sleep(step)

# 0V for 10 secs
kit.motor1.throttle = 0
sleep(10)

# End

'''for i in range(50):
    kit.motor1.throttle = 1.0 - 2*(i/50)
    sleep(0.1)
        
kit.motor1.throttle = None
sleep(1)
kit.motor1.throttle = -0.5
sleep(2)
kit.motor1.throttle = None
sleep(1)
kit.motor1.throttle = 0.0

kit.motor2.throttle = 0.5
sleep(1)
kit.motor2.throttle = None
sleep(1)
kit.motor2.throttle = 0.0

kit.motor3.throttle = 0.5
sleep(1)
kit.motor3.throttle = None
sleep(1)
kit.motor3.throttle = 0.0
'''

print('Done')
quit()