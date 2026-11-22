from main import calculate_grade, calculate_average

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_F():
    assert calculate_grade(30) == "F"

def test_average():
    assert calculate_average([80, 90, 100]) == 90