import pytest
from student import CheckName, Student


@pytest.fixture
def ch1():
    return CheckName()


@pytest.fixture
def s1():
    return Student('Ivan', 'Ivanov', 'Ivanovich', 'sub.csv')


def test_check_name(ch1):
    assert ch1.validate('Ivanov') == 'Ivanov', 'Test nom.1 failed'


def test_open_csv(s1):
    assert s1.sub_from_csv('sub.csv') == ['math', 'English', 'physics', 'biology', 'chemistry', 'history']


def test_add_grade(s1):
    s1.add_grades('math', 2)
    assert s1.grades == {'math': [2], 'English': [], 'physics': [], 'biology': [], 'chemistry': [], 'history': []}



if __name__ == '__main__':
    pytest.main(['-vv'])

