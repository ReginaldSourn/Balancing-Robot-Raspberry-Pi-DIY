import RPi.GPIO as GPIO
import time
import socket
import smbus
import math

import multiprocessing
class hardwaredriver(object):
    stp1 = 21
    dir1 = 20
    en1 = 6

    stp2 = 16
    dir2= 12
    en2 = 5
    def __init__(self):
        self.stp1 = 21
        self.dir1 = 20
        self.en1 = 6

        self.stp2 = 16
        self.dir2= 12
        self.en2 = 5
        ''' this driver code'''
        GPIO.setmode(GPIO.BCM)
        #STEPPER ONE RIGHT

        #stepper 1 register.
        GPIO.setup(self.stp1,GPIO.OUT)
        GPIO.setups(self.dir1,GPIO.OUT)
        GPIO.setup(self.en1,GPIO.OUT)
        #STEPPER ONE LEFT

        GPIO.setup(self.stp2, GPIO.OUT) #ENABLE 2
        GPIO.setup(self.dir2), GPIO.OUT)  # STEP 2
        GPIO.setup(self.en2, GPIO.OUT)#DIR 2


    def motor1_mv_fw(self, step, speed):
        self.motor1En()
        GPIO.output(en1, 0)
        GPIO.output(dir1, 1)
        for x in range (0, step):
            GPIO.output(stp1, 1 )
            sleep(speed)
            GPIO.output(stp1, 0)
            sleep(speed)
        self.motor1Disable()

    def motor1_mv_bw(self, step, speed):
        self.motor1En()
        GPIO.output(self.en1, 0)
        GPIO.output(self.dir1, 0)
        for x in range (0, step):
            GPIO.output(self.stp1, 1 )
            sleep(speed)
            GPIO.output(self.stp1, 0)
            sleep(speed)
        self.motor1Disable()
    def motor2_mv_bw(self, step, speed):
        sefl.motor2En()
        GPIO.output(self.en2, 0)
        GPIO.output(self.dir2, 0)
        for x in range (0, step):
            GPIO.output(self.stp2, 1 )
            sleep(speed)
            GPIO.output(self.stp2, 0)
            sleep(speed)
        self.motor2Disable()


    def motor2_mv_fw(self, step, speed):
        motor2En()
        GPIO.output(self.en2, 0)
        GPIO.output(self.dir2, 1)
        for x in range (0, step):
            GPIO.output(self.stp2, 1 )
            sleep(speed)
            GPIO.output(self.stp2, 0)
            sleep(speed)
        self.motor2Disable()
    def motor1En(self):
        GPIO.output(self.en1, 0)
    def motor2En(self):
        GPIO.output(self.en2, 0)
    def motor1Disable(self):
        GPIO.output(self.en1,1)
    def motor2Disable(self):
        GPIO.output(self.en2, 1)
class readingMPU(object):
    def __init__(self):
        self.bus = smbus.SMBUS(1)
        self.address = 0x68
    def read_byte(adr):
        return bus.read_byte_data(address, adr)

    def read_word(adr):
        high = bus.read_byte_data(address, adr)
        low = bus.read_byte_data(address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(adr):
        val = read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)
    def x_value():

class Balancer(object):

    def __init__(self, setpoint=0):
        self.setpoint = setpoint
        self.sensorValue =0

    def calculatePID(self):
        ''' not yet complete function'''

        error = self.sensorValue - self.setpoint
        self.proportional = error
        self.intergral += error * dt
        self.derivative = (error - previousError)/dt;

        previousError = error;

        speed = proportional*kp + intergral*ki + derivative*kd
    def movement calcultation(self):
        
class ReadFromSocket(socket):
    s = soc


def main():

    print("main")
