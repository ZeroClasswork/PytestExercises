# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.
import math
import pytest

def display_grade_stat():
    """Gathers stats and print them out."""
    grade_list = read_input()
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

# display_grade_stat()

@pytest.fixture
def high_grades():
    return [98, 97, 100, 83, 90, 87, 98, 100]

@pytest.fixture
def med_grades():
    return [98, 54, 59, 83, 80, 76, 62, 77]

def test_high_grades_calculate_stat(high_grades):
    mean, std_dev = calculate_stat(high_grades)
    assert math.isclose(mean, 94.125)
    assert math.isclose(std_dev, 6.1122316, abs_tol=0.0001)

def test_med_grades_calculate_stat(med_grades):
    mean, std_dev = calculate_stat(med_grades)
    assert math.isclose(mean, 73.625)
    assert math.isclose(std_dev, 13.573296, abs_tol=0.0001)