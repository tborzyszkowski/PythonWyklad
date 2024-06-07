from .sensor import Sensor


class Alarm:

    def __init__(self, sensor=None):
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = sensor or Sensor()
        self._is_alarm_on = False
        
    def check(self):
        pressure = self._sensor.sample_pressure()
        if pressure < self._low_pressure_threshold \
                or self._high_pressure_threshold < pressure:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
