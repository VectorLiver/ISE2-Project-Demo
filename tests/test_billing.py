from src.billing import calculate_bill

def test_calculate_bill():
    assert calculate_bill(100, 0.1) == 110
