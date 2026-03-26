"""FRED API module for risk-free rate"""
import requests
from wacc_builder.data import DEFAULT_RF


def fetch_rf_from_fred(series="DGS10", api_key=None):
    if api_key is None: return None
    try:
        r = requests.get("https://api.stlouisfed.org/fred/series/observations",
            params={"series_id":series,"api_key":api_key,"file_type":"json","limit":1,"sort_order":"desc"}, timeout=10)
        d = r.json()
        if d.get("observations"):
            v = d["observations"][0].get("value",".")
            if v != ".": return float(v) / 100.0
    except Exception: pass
    return None
