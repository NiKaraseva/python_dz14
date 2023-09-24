class MyException(Exception):
    pass

class InvalidNameException(MyException):
    def __init__(self):
        self.message = f'Invalid value: full name should be istitle and isalpha'
        super().__init__(self.message)

class InvalidSubjectException(MyException):
    def __init__(self, subject_name: str):
        self.message = f'Subject {subject_name} not found'
        super().__init__(self.message)


class InvalidGradeException(MyException):
    def __init__(self, grade_res: int):
        self.message = f'Grade {grade_res} is invalid, it should be between 2 and 5'
        super().__init__(self.message)


class InvalidTestResException(MyException):
    def __init__(self, test_res: int):
        self.message = f'Grade {test_res} is invalid, it should be between 0 and 100'
        super().__init__(self.message)