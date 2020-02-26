import pytest
import System

def test_create_assignment(grading_system):
    grading_system.login('goggins','augurrox')
    assignment_name = 'assignment9000'
    course_name = 'software_engineering'
    grading_system.usr.create_assignment(assignment_name, '4/22/20', course_name)
    grading_system.reload_data()
    assert assignment_name in grading_system.courses[course_name]['assignments']


@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
