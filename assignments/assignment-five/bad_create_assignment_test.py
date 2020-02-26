import pytest
import System

def test_bad_create_assignment(grading_system):
    #sign in with staff
    grading_system.login('goggins', 'augurrox')
    
    #create an assignment
    grading_system.usr.create_assignment('assignment3', '2/15/20', 'comp_sci')
    grading_system.reload_data()

    #assignment cannot be created in a course the user does not manage
    assert 'assignment3' not in grading_system.courses['comp_sci']['assignments']
    

@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
