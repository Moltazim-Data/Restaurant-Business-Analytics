from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from analysis import load_data, validate_data

def test_data_quality():
    orders, items, menu, staffing = load_data()
    assert all(validate_data(orders, items, menu, staffing).values())
    assert len(orders) > 1000 and len(items) > len(orders)
