import pytest
import System



def test_bad_check_grades(grading_system):
    

    #set target user, course, and assignment
    user = 'akend3'
    course = 'databases'
    
   
    #login to TA user
    grading_system.login('cmhbf5', 'bestTA')

    #check grades of student not enrolled in TA's course. If return is longer than 0, test fails. 
    #TA's should not be able to check other students' grades
    if len(grading_system.usr.check_grades(user, course)) > 0:
        assert False
    
    
    

@pytest.fixture
def grading_system():
    grading_system = System.System();
    grading_system.load_data()
    return grading_system
