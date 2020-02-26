import System
import pytest


def test_check_password(grading_system):
    assert grading_system.check_password('akend3', '123454321')==True
    assert grading_system.check_password('hdjsr7', 'pass1234')==True
    assert grading_system.check_password('yted91', 'imoutofpasswordnames')==True
    assert grading_system.check_password('calyam', '#yeet')==True
    assert grading_system.check_password('cmhbf5', 'bestTA')==True




@pytest.fixture
def grading_system():
    grading_system = System.System()
    grading_system.load_data
    return grading_system
