# See: Unit Testing with Python By Emily Bache @ pluralsight.com


import unittest

from _0B_tdd.telemetry import *


class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_check_transmission_should_send_a_diagnostic_message_and_receive_a_status_message_response(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=True,
                                                                   receive_data="foo"))
        controls.check_transmission()
        self.assertEqual("foo", controls.diagnostic_info)

    def test_check_transmission_fails_if_telemetry_client_doesnt_connect(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=False,
                                                                   receive_data="foo",))
        self.assertRaises(Exception, controls.check_transmission) 
        self.assertEqual("", controls.diagnostic_info)

    def test_check_transmission_fails_if_telemetry_client_disconnects_before_receive(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=True,
                                                                   receive_data="foo",
                                                                   go_offline_on_send=True))
        self.assertRaises(Exception, controls.check_transmission) 
        self.assertEqual("", controls.diagnostic_info)

    def test_retry_connection_three_times_before_raising_an_exception(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=False,
                                                                   receive_data="foo",
                                                                   go_online_on_third_attempt=True))
        controls.check_transmission()
        self.assertEqual("foo", controls.diagnostic_info)


class MockTelemetryClient:

    def __init__(self, online, receive_data="", go_offline_on_send=False, go_online_on_third_attempt=False):
        self.online_status = online
        self.receive_data = receive_data
        self.go_offline_on_send = go_offline_on_send
        self.go_online_on_third_attempt = go_online_on_third_attempt
        self.attempts = 0

    def send(self, message):
        if self.go_offline_on_send:
            self.online_status = False

    def connect(self, connection_string):
        self.attempts += 1
        if self.go_online_on_third_attempt and self.attempts == 2:
            self.online_status = True

    def receive(self):
        if self.online_status:
            return self.receive_data
        else:
            raise Exception("Not online")

    def disconnect(self):
        pass

    def get_online_status(self):
        return self.online_status


if __name__ == '__main__':
    unittest.main()