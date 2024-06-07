import unittest
from unittest.mock import patch, Mock

from alarm import Alarm


class AlarmPreasureMonkeypatchTests(unittest.TestCase):
    def test_alarm_with_high_pressure_value(self):
        with patch('alarm.Sensor') as test_sensor_class:
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 22
            test_sensor_class.return_value = test_sensor_instance

            alarm = Alarm()
            alarm.check()

            assert alarm.is_alarm_on


    @patch('alarm.Sensor')
    def test_alarm_with_too_low_pressure_value(self, test_sensor_class):
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 16
        test_sensor_class.return_value = test_sensor_instance

        alarm = Alarm()
        alarm.check()

        assert alarm.is_alarm_on
