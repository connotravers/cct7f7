import pytest
import System


#Tests if the program can add a new user given new username and password using the login function
def test_login(grading_system):
    username = 'goggins'
    password = 'augurrox'

    #login
    grading_system.login(username,password)
    #the user which logged in should be the current user
    assert grading_system.usr.name == username
    

    
@pytest.fixture
def grading_system():
    grading_system  = System.System()
    grading_system.load_data()
    return grading_system




