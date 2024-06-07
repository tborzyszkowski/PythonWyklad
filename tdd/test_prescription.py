# See: Unit Testing with Python By Emily Bache @ pluralsight.com


import unittest
from datetime import date, timedelta

from src.tdd.prescription import Prescription


def days_ago(days):
    return date.today() - timedelta(days=days)


class TestPrescription(unittest.TestCase):
    
    def test_days_taken_excludes_future_dates(self):
        prescription = Prescription("Codeine",
                                    dispense_date = days_ago(days=2),
                                    days_supply=4)
        self.assertListEqual([days_ago(2), days_ago(1)],
                             list(prescription.days_taken()))
