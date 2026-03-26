"""
Data: sector betas, risk premiums, country risk
Damodaran (Stern NYU), March 2026
#"""

DAMODAR_BETAS = {
    "ter": (0.62, "Water Utility"),
    "water_utility": (0.62, "Water Utility (regulated)"),
    "water_infrastructure": (0.79, "Water Infrastructure (EM, PPP)"),
    "renewable_energy": (0.83, "Renewable Energy"),
    "toll_road": (0.78, "Toll Road"),
    "wastewater": (0.65, "Wastewater Treatment"),
    "desalination": (0.82, "Desalination Plant"),
    "power_generation": (0.85, "Power Generation"),
    "gas_distribution": (0.68, "Gas Distribution"),
    "telecom": (0.75, "Telecommunications"),
    "ports": (0.77, "Ports & Terminals"),
}

DAMODAANERP = {
    "US": 0.0460,
    "Mature Market": 0.0460,
    "Global": 0.0508,
    "Emerging Markets": 0.0508,
}

COUNTRY_RISK_PREMIUM = {
    "MX": (0.0246, "Mexico — Ba2"),
    "BR": (0.0472, "Brazil — Ba3"),
    "CL": (0.0062, "Chile — A1"),
    "PE": (0.0148, "Peru — Baa3"),
    "CO": (0.0211, "Colombia — Baa2"),
    "AR": (0.1842, "Argentina — Ca"),
    "US": (0.0000, "United States — Aaa"),
}

GREENFIELD_PREMIUM = {
    "greenfield_swro": 0.015,
    "brownfield": 0.005,
    "operating_concession": 0.0,
    "ppp_availability": 0.010,
}

ILLIQUIDITY_PREMIUM = {
    "small": 0.020,
    "mid": 0.010,
    "large": 0.005,
}

DEFAULT_RF = 0.0430
