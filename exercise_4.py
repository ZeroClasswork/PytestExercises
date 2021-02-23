# by Kami Bigdely
# Replace nested conditional with gaurd clauses

import pytest

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else:
                pos = None
    return pos

# if __name__ == "__main__":
#     result1 = extract_position('|error| numerical calculations could not converge.')
#     print(result1)
#     result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
#     print(result2)

@pytest.fixture
def error_position():
    return "error error x:453453.234"

@pytest.fixture
def debug_position():
    return "debugging...x:3423.424"

@pytest.fixture
def valid_position():
    return "x:343.23423452345"

def test_extract_position_error(error_position):
    assert extract_position(error_position) == None

def test_extract_position_debug(debug_position):
    assert extract_position(debug_position) == None

def test_extract_position_valid(valid_position):
    assert extract_position(valid_position) == "343.23423452345"
