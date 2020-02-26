import pytest
import System

#a bad password will not work
def test_bad_check_password(grading_system):
    assert grading_system.check_password('goggins', 'auguriscool')
    

@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data()
    return grading_system
