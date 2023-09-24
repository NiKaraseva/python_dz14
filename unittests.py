import unittest
from student import CheckName, Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.ch1 = CheckName()
        self.s1 = Student('Ivan', 'Ivanov', 'Ivanovich', 'sub.csv')
        self.s1.grades = {'math': [3, 4], 'English': [], 'physics': [], 'biology': [], 'chemistry': [], 'history': []}


    def test_check_name(self):
        self.assertEqual(self.ch1.validate('Ivanov'), 'Ivanov')


    def test_open_csv(self):
        self.assertEqual(self.s1.sub_from_csv('sub.csv'),
                         ['math', 'English', 'physics', 'biology', 'chemistry', 'history'])


    def test_add_grades(self):
        self.s1.add_grades('math', 2)
        self.assertEqual(self.s1.grades, {'math': [3, 4, 2], 'English': [], 'physics': [], 'biology': [], 'chemistry': [], 'history': []})


    def test_average_grade(self):
        self.assertEqual(self.s1.average_grade(), 3.5)



if __name__ == '__main__':
    unittest.main(verbosity=2)