import logging

logging.basicConfig(level=logging.INFO)

def calculate_risk_score(age: int, balance: float) -> float:
    """Calculates a simulated financial risk score."""
    if age < 18:
        logging.warning("Underage access attempt.")
        raise ValueError("Must be 18 or older.")
    return balance / (age * 0.1)