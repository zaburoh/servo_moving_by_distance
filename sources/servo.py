import pigpio

class Servo():
  """ 500 ~ 2500まで！"""
  def __init__(self):
    self.SERVO_PIN = 23
    self.pi = pigpio.pi()
  
  def move(self, pulse):
    self.pi.set_servo_pulsewidth(self.SERVO_PIN, pulse)

