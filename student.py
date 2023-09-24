import csv
from my_exception import (InvalidNameException, InvalidSubjectException,
                          InvalidGradeException, InvalidTestResException)


class CheckName:

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)\

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        """A function that checks a name for letters and a capital first letter:

        >>> name = CheckName()
        >>> name.validate('Ivan')
        'Ivan'

        >>> surname = CheckName()
        >>> surname.validate('Ivanov')
        'Ivanov'"""

        if value.isalpha() and value.istitle():
            return value
        else:
            raise InvalidNameException()


class Student:

    def __init__(self, name: str, surname: str, patronymic: str, file_name: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.subjects = self.sub_from_csv(file_name)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}


    def sub_from_csv(self, file_name: str):
        """A function that load subjects from csv file:

        >>> s1 = Student('Ivan', 'Ivanov', 'Ivanovich', 'sub.csv')
        >>> s1.sub_from_csv('sub.csv')
        ['math', 'English', 'physics', 'biology', 'chemistry', 'history']
        """

        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            return next(reader)


    def __str__(self):
        return f'Student: name = {self.name}, surname = {self.surname}, patronymic = {self.patronymic}'


    def add_grades(self, subject: str, grade: int):
        """Function that adds grades to items:

        >>> s1 = Student('Ivan', 'Ivanov', 'Ivanovich', 'sub.csv')
        >>> s1.add_grades('math', 3)
        >>> s1.add_grades('math', 5)

        >>> s2 = Student('Petr', 'Petrov', 'Petrovich', 'sub.csv')
        >>> s2.add_grades('English', 5)
        """

        if subject not in self.subjects:
            raise InvalidSubjectException(subject)
        if 2 > grade or grade > 5:
            raise InvalidGradeException('No')
        self.grades[subject].append(grade)


    def add_test_results(self, subject: str, t_res: int):
        if subject not in self.subjects:
            raise InvalidSubjectException(subject)
        if 0 > t_res or t_res > 100:
            raise InvalidTestResException(t_res)
        self.test_results[subject].append(t_res)


    def average_grade(self):
        sum_grade = sum([sum(grade) for grade in self.grades.values()])
        sum_sub = sum([len(grade) for grade in self.grades.values()])
        if sum_sub:
            return sum_grade / sum_sub


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)