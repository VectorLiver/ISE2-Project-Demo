import pytest
from src.core_logic import calculate_risk_score

def test_valid_calculation():
    assert calculate_risk_score(20, 1000) == 500.0

def test_underage_error():
    with pytest.raises(ValueError):
        calculate_risk_score(17, 1000)