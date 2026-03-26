"""WACC analysis for Mexico SWRO projects"""
from wacc_builder.model import WACCModel, compare_countries
from wacc_builder.charts import plot_waterfall, plot_country_comparison
from tabulate import tabulate


def main():
    scenarios = [
        {"name":"Sc 1 - Conservative","sector":"desalination","country":"MX","debt_ratio":0.45,"equity_ratio":0.55,"kd_pretax":0.055,"project_type":"greenfield_swro","size_bucket":"mid"},
        {"name":"Sc 2 - Base Case","sector":"desalination","country":"MX","debt_ratio":0.65,"equity_ratio":0.35,"kd_pretax":0.065,"project_type":"ppp_availability","size_bucket":"mid"},
        {"name":"Sc 3 - High Leverage","sector":"desalination","country":"MX","debt_ratio":0.75,"equity_ratio":0.25,"kd_pretax":0.075,"project_type":"ppp_availability","size_bucket":"mid"},
        {"name":"Sc 4 - Operating Concession","sector":"water_infrastructure","country":"MX","debt_ratio":0.70,"equity_ratio":0.30,"kd_pretax":0.055,"project_type":"operating_concession","size_bucket":"large"},
        {"name":"Sc 5 - Small Greenfield","sector":"desalination","country":"MX","debt_ratio":0.60,"equity_ratio":0.40,"kd_pretax":0.070,"project_type":"greenfield_swro","size_bucket":"small"},
    ]

    print("\nMEXICO SWRO WACC ANALRÉLSI\n" + "="*60)
    rows = []
    models = []
    for s in scenarios:
        name = s.pop("name")
        m = WACCModel(**s)
        models.append((name, m))
        rows.append({"Scenario": name, "D/V": f"{m.debt_ratio:.0%}", "Ke": f"{m.ke_total:.2%}", "Kd AT": f"{m.kd_aftertax:.2%}", "WACC": f"{m.wacc:.2%}"})
    print(tabulate(rows, headers="keys", tablefmt="grid"))

    print("\nDETAILED: Base Case")
    models[1][1].print_summary()

    plot_waterfall(models[1][1], save_path="mexico_swro_wacc_waterfall.png")
    plot_country_comparison(sector="desalination", save_path="mexico_swro_country_comparison.png")


if __name__ == "__main__":
    main()
