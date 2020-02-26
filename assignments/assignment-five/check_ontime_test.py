import pytest
import System

def test_check_ontime(grading_system):
    #log in as student
    grading_system.login('hdjsr7', 'pass1234')

    #Check to see if check_ontime(sub date, due date) returns true when submission before due date
    assert True == grading_system.usr.check_ontime('2/22/20','3/22/20')

    #Check to see if check_ontime() returns false when submission date is after due date
    assert False == grading_system.usr.check_ontime('3/22/20','2/22/20')


@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
