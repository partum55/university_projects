"""dvv_oop_script"""

import dvv


class Course:
    def __init__(self):
        ...


class Student:
    def __init__(self):
        ...


class RegistrationProcessor:
    def __init__(self):
        ...


if __name__ == '__main__':
    processor = RegistrationProcessor('mini_registrations.txt', 'courses_data.json')
    assert str(processor.students) == '[Mary Miller, Robert Rodriguezes, Linda Wilson]'
    assert set(dvv.read_file('mini_registrations.txt').keys()) == {student.name for student in processor.students}
    assert dvv.read_file('mini_registrations.txt') == {student.name: {'Number': student.number, 'Scores':student.scores, 'Prioritization': student.prioritization} for student in processor.students}
    assert dvv.PREREQUISITES == {course.name: course.prerequisites for course in processor.courses}
    assert dvv.CAPACITY == {course.name: course.capacity for course in processor.courses}
