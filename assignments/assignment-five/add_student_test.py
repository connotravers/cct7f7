import pytest
import System

def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('akend3', 'software_engineering')
    grading_system.reload_data()
    grading_system.load_data()
    
    assert 'software_engineering' in grading_system.users['akend3']['courses']

@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
