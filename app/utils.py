from typing import List


def get_average_rate(rates: List[str]) -> float:
    parsed_rates = [float(rate) for rate in rates if rate]
    avg_rate = sum(parsed_rates) / len(rates)
    return round(avg_rate, 3)
