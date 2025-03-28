# Work by Esconde, Kharlein Kaye B.
import pytest
from datetime import datetime, timedelta
from project import compute_daily_output, compute_total_work_days, compute_end_date

def test_compute_daily_output():
    assert compute_daily_output(10, 8) == 80  # 10 units per hour * 8 hours
    assert compute_daily_output(20, 6) == 120  # 20 units per hour * 6 hours
    assert compute_daily_output(0, 8) == 0  # 0 output per hour

def test_compute_total_work_days():
    assert compute_total_work_days(1000, 100) == 10  # 1000 units, 100 units per day
    assert compute_total_work_days(1001, 100) == 11  # One extra day needed
    assert compute_total_work_days(500, 200) == 3  # 500 units, 200 units per day

def test_compute_end_date():
    start_date = datetime(2025, 3, 1)  # March 1, 2025
    
    # 5-day workweek (Monday-Friday)
    assert compute_end_date(start_date, 6, 5) == datetime(2025, 3, 10)  # Should finish on March 7
    assert compute_end_date(start_date, 10, 5) == datetime(2025, 3, 14)  # Should finish on March 14
    
    # 6-day workweek (Monday-Saturday)
    assert compute_end_date(start_date, 5, 6) == datetime(2025, 3, 6)  # Should finish on March 6
    assert compute_end_date(start_date, 10, 6) == datetime(2025, 3, 12)  # Should finish on March 13
    
    # 7-day workweek (Monday-Sunday)
    assert compute_end_date(start_date, 5, 7) == datetime(2025, 3, 5)  # Should finish on March 5
    assert compute_end_date(start_date, 10, 7) == datetime(2025, 3, 10)  # Should finish on March 10
