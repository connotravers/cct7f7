import pytest
import System

def test_view_assignments(grading_system):
    #make variables to use
    username='akend3'
    course_get='databases'

    #login as a student
    grading_system.login(username, '123454321')

    #get assignments for databases
    my_assignments = grading_system.usr.view_assignments(course_get)

    #for each assignment returned, check that the assignment is in the correct course for the correct student
    #and then check if the due date is correct
    for an_ass in my_assignments:
        assert an_ass[0] in grading_system.courses[course_get]['assignments']
        assert an_ass[1] == grading_system.courses[course_get]['assignments'][an_ass[0]]['due_date']



@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
