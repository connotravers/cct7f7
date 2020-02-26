import pytest
import System
#test that you cannot log in with a fake user and real pass
def test_bad_login(grading_system):
    #attempt to sign in using bad login
    grading_system.login('sample', '123454321')
    assert 'sample' == grading_system.usr.name




@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
