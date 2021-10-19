import json 
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

ledPin = 19 # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False) # ignore warnings due to multiple scripts at same time

pwm = GPIO.PWM(ledPin, 100) # PWM object on our pin at 100 Hz
pwm.start(0) # start with LED off

while True:
  with open("led_pwm.txt", 'r') as f:
    dutyCycle = json.load(f)
    #dutyCycle = float(f.read()) # read duty cycle value from file
  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)

