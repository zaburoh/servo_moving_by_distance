import VL53L1X

class Distance():
  def __init__(self, bus, address):
    self.UPDATE_TIME_MICROS = 66000
    self.INTER_MEASUREMENT_PERIOD_MILLIS = 70
    self.i2c_bus = bus
    self.i2c_address = address

    self.tof = VL53L1X.VL53L1X(self.i2c_bus, self.i2c_address)

  def start(self):
    self.tof.open()
    self.tof.set_timing(self.UPDATE_TIME_MICROS, self.INTER_MEASUREMENT_PERIOD_MILLIS)
    self.tof.start_ranging(0)


