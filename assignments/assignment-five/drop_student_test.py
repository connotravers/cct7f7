import pytest
import System

def test_drop_student(grading_system):
    course_to_drop = 'comp_sci'
    student_to_drop = 'akend3'
    grading_system.login('saab', 'boomr345')
    assert course_to_drop in grading_system.users['akend3']['courses'], 'The student is not currently enrolled in this course'
    grading_system.usr.drop_student(student_to_drop, course_to_drop)
    grading_system.reload_data()
    assert course_to_drop not in grading_system.users['akend3']['courses'], 'The student has not been dropped from the course'




@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
