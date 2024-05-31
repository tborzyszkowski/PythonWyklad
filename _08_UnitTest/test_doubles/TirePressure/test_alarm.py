import unittest
from unittest.mock import Mock

from src.test_doubles.TirePressure.alarm import Alarm
from src.test_doubles.TirePressure.sensor import Sensor

class StubSensor:
    def sample_pressure(self):
        return 15

class AlarmPreasureTests(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_low_pressure_activates_alarm(self):
        alarm = Alarm(sensor=StubSensor())
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_normal_pressure_alarm_stays_off(self):
        stub_sensor = Mock(Sensor)
        stub_sensor.sample_pressure.return_value = 18
        alarm = Alarm(sensor=stub_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

