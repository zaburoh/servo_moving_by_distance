import sys
import signal
from distance import Distance
from servo import Servo

def exit_handler(signal, frame):
  print("\n>> exit handler")
  dist.tof.stop_ranging()
  sys.stdout.write("\n")
  sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

servo = Servo()
dist = Distance(1, 0x29)
dist.start()

def carriage_return():
  sys.stdout.write("\r")
  sys.stdout.flush()  

def distance_to_pulse(distance):
  """ distance is cm """
  return int((distance / 70) * 1900 + 500)

def get_distance_cm():
  return dist.tof.get_distance() / 10.0

def move_by_distance(distance_cm):
  pulse = distance_to_pulse(distance_cm)

  if pulse < 500:
    pulse = 500
  elif 2400 < pulse:
    pulse = 2400
  else:
    pulse = pulse

  servo.move(pulse)
  return pulse

def current_value_print():
  sys.stdout.write(u"{:04.1f}cm {} pulse".format(distance_cm, pulse))
  sys.stdout.flush()

while True:
  distance_cm = get_distance_cm()
  pulse = move_by_distance(distance_cm)
  carriage_return()
  current_value_print()
  