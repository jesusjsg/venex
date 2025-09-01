from typing import List, Optional


def get_average_rate(rates: List[str]) -> float:
    parsed_rates = [float(rate) for rate in rates if rate]
    if not parsed_rates:
        return 0.0
    avg_rate = sum(parsed_rates) / len(parsed_rates)
    return round(avg_rate, 3)


def get_percent_change(
    current_rate: float, last_rate: Optional[float]
) -> Optional[float]:
    if last_rate is None or last_rate == 0:
        return None
    return ((current_rate - last_rate) / last_rate) * 100


def get_diff(current_rate: float, last_rate: Optional[float]) -> Optional[float]:
    if last_rate is None:
        return None
    return round(current_rate - last_rate, 4)
