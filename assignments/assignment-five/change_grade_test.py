import pytest
import System

def test_change_grade(grading_system):
    #Login as a TA
    grading_system.login('cmhbf5', 'bestTA')
    #change the grade 
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 50)
    
    #store the new grade in the database
    grading_system.reload_data()
    
    #check that the new grade was stored
    assert grading_system.users['yted91']['courses']['software_engineering']['assignment1']['grade'] == 50



@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
