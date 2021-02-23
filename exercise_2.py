import math

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
    in the sample conpared to the amount in living
    tissue (unitless).
    """
    if carbon_14_ratio > 1 or carbon_14_ratio <= 0:
        return None
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF

def test_get_age_carbon_14_dating():
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34, abs_tol=0.01)
    assert get_age_carbon_14_dating(0) == None
    assert get_age_carbon_14_dating(3) == None
    assert get_age_carbon_14_dating(34.2) == None
    assert get_age_carbon_14_dating(-12.34) == None
    assert get_age_carbon_14_dating(-0.34) == None