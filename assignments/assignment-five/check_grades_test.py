import pytest
import System

def test_check_grades(grading_system):
    
    #Set variables to use and login as student
    username = 'yted91'
    #check software_engineering
    course_check = 'software_engineering'
    grading_system.login('yted91', 'imoutofpasswordnames')
    
    #Call to check grades
    grades = grading_system.usr.check_grades(course_check)
    
    #For each assignment in the returned grades, check that the assignment exists and then check if the grade
    #is the same as the grade returned from check_grades
    for an_ass in grades:
        assert an_ass[0] in grading_system.users[username]['courses'][course_check]
        assert an_ass[1] == grading_system.users[username]['courses'][course_check][an_ass[0]]['grade']


@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
