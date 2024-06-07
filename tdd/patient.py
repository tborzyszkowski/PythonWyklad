# See: Unit Testing with Python By Emily Bache @ pluralsight.com


class Patient:

    def __init__(self, prescriptions=None):
        self.prescriptions = prescriptions or []

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

    def days_taking(self, medicine_name):
        prescriptions = filter(lambda p: p.name == medicine_name, self.prescriptions)
        days = set()
        for prescription in prescriptions:
            days.update(prescription.days_taken())
        return days

    def clash(self, medicine_names):
        days_taking = [self.days_taking(medicine_name)
                       for medicine_name in medicine_names] \
                      or [set()]
        return set.intersection(*days_taking)
