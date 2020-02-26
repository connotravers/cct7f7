import pytest
import System


def test_submit_assignment(grading_system):
        #set the variables we are going to use
    assignment = 'assignment3'
    course = 'cloud_computing'
    username = 'hdjsr7'
    submission = 'ooo yeah!'
    submit_date = '3/25/20'
        
        #login as student
    grading_system.login(username, 'pass1234')
    
        #submit the assignment and reload data from the updated database
    grading_system.usr.submit_assignment(course, assignment,submission,submit_date)
    grading_system.reload_data()

    assert assignment in grading_system.users[username]['courses'][course]
    assert submission == grading_system.users[username]['courses'][course][assignment]['submission']
    assert submit_date == grading_system.users[username]['courses'][course]['submission_date']

@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
