import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def test_full_name(self):
        print('test full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_email(self):
        print('test email')
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_alert_santa(self):
        print('test alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_apply_extension(self):
        return self

  
if __name__ == '__main__':
    unittest.main()
