import random


class Sensor(object):
    # The reading of the pressure value from the sensor is simulated.
    # The focus of the example is on the other class.

    _OFFSET = 16

    def sample_pressure(self):
        pressure_telemetry_value = self.simulate_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def simulate_pressure():
        # simulates a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value
