import unittest

from context import oop


class PersonTestCase(unittest.TestCase):

    def test_person_name_correctly_initialized(self):
        person = oop.Person("John")
        self.assertEqual("John", person.name)

    def test_person_name_correctly_changed(self):
        # Arrange
        person = oop.Person("John")
        # Act
        person.rename("Jan")
        # Assert
        self.assertEqual("Jan", person.name)

    def test_persons_are_the_same_species(self):
        personAdam = oop.Person("Adam")
        personEwa = oop.Person("Ewa")
        self.assertEqual(personAdam.species, personEwa.species)


if __name__ == '__main__':
    unittest.main()
