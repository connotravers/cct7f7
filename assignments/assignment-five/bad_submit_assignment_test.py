import pytest
import System


#attempts to submit an assignment that doesn't exist
def test_bad_submit_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')

    grading_system.usr.submit_assignment('cloud_computing','assernamente123', 'Oopsies', '2/21/20')



@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
