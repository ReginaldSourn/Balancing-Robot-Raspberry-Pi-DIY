import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

stp1 = 21
dir1 = 20
en1 = 6

stp2 = 16
dir2= 12
en2 = 5


#stepper 1 register.
GPIO.setup(stp1,GPIO.OUT)
GPIO.setup(dir1,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

#stepper 2 register.
GPIO.setup(stp2,GPIO.OUT)
GPIO.setup(dir2,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)


def motor1_mv_fw(step, speed):

    GPIO.output(en1, 0)
    GPIO.output(dir1, 1)
    for x in range (0, step):
        GPIO.output(stp1, 1 )
        sleep(speed)
        GPIO.output(stp1, 0)
        sleep(speed)


def motor1_mv_bw(step, speed):

    GPIO.output(en1, 0)
    GPIO.output(dir1, 0)
    for x in range (0, step):
        GPIO.output(stp1, 1 )
        sleep(speed)
        GPIO.output(stp1, 0)
        sleep(speed)

def motor2_mv_bw(step, speed):

    GPIO.output(en2, 0)
    GPIO.output(dir2, 0)
    for x in range (0, step):
        GPIO.output(stp2, 1 )
        sleep(speed)
        GPIO.output(stp2, 0)
        sleep(speed)



def motor2_mv_fw(step, speed):

    GPIO.output(en2, 0)
    GPIO.output(dir2, 1)
    for x in range (0, step):
        GPIO.output(stp2, 1 )
        sleep(speed)
        GPIO.output(stp2, 0)
        sleep(speed)
def motor1En():
    GPIO.output(en1, 0)
def motor2En():
    GPIO.output(en2, 0)

def motor1Disable():
    GPIO.output(en1,1)
def motor2Disable():
    GPIO.output(en2, 1)

def main():
#    motor1Disable()
    while 1:
        motor1En()
        
        motor1_mv_fw(300, 0.001)
        motor1Disable()
        motor2En()
        motor2_mv_fw(300, 0.001)
        motor2Disable()
        sleep(0.5)
        motor1En()
        motor1_mv_bw(300, 0.001)
        motor1Disable()
        motor2En()
        motor2_mv_bw(300, 0.001)
        motor2Disable()
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        motor1Disable()
        motor2Disable()
        GPIO.cleanup()
