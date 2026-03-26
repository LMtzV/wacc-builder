"""CLI for WACC Builder"""
import argparse
import sys
from wacc_builder.model import WACCModel, compare_countries, compare_sectors
from wacc_builder.charts import plot_waterfall, plot_country_comparison


def main():
    parser = argparse.ArgumentParser(description="WACC Builder")
    sub = parser.add_subparsers(dest="cmd")

    bp = sub.add_parser("build")
    bp.add_argument("--sector", default="water_infrastructure")
    bp.add_argument("--country", default="MX")
    bp.add_argument("--debt-ratio", type=float, default=0.65)
    bp.add_argument("--kd", type=float, default=0.065)
    bp.add_argument("--tax-rate", type=float, default=0.30)
    bp.add_argument("--project-type", default="ppp_availability")
    bp.add_argument("--size-bucket", default="mid")
    bp.add_argument("--chart", action="store_true")
    bp.add_argument("--save-chart", default=None)
    bp.add_argument("--fred-key", default=None)
    bp.add_argument("--no-greenfield", dest="include_greenfield", action="store_false")
    bp.add_argument("--no-illiquidity", dest="include_illiquidity", action="store_false")

    cp = sub.add_parser("compare-countries")
    cp.add_argument("--sector", default="water_infrastructure")
    cp.add_argument("--debt-ratio", type=float, default=0.65)
    cp.add_argument("--kd", type=float, default=0.065)
    cp.add_argument("--tax-rate", type=float, default=0.30)
    cp.add_argument("--chart", action="store_true")
    cp.add_argument("--save-chart", default=None)

    sp = sub.add_parser("compare-sectors")
    sp.add_argument("--country", default="MX")
    sp.add_argument("--debt-ratio", type=float, default=0.65)
    sp.add_argument("--kd", type=float, default=0.065)
    sp.add_argument("--tax-rate", type=float, default=0.30)

    args = parser.parse_args()
    if not hasattr(args, 'cmd') or args.cmd is None:
        parser.print_help(); return 0

    if args.cmd == "build":
        m = WACCModel(sector=args.sector, country=args.country, debt_ratio=args.debt_ratio, equity_ratio=1-args.debt_ratio, kd_pretax=args.kd, tax_rate=args.tax_rate, project_type=args.project_type, size_bucket=args.size_bucket, include_greenfield=args.include_greenfield, include_illiquidity=args.include_illiquidity, fred_api_key=args.fred_key)
        m.print_summary(); print(f"\nWACC = {m.wacc:.2%}")
        if args.chart: plot_waterfall(m, save_path=args.save_chart or "wacc.waterfall.png")
    elif args.cmd == "compare-countries":
        compare_countries(sector=args.sector, debt_ratio=args.debt_ratio, equity_ratio=1-args.debt_ratio, kd_pretax=args.kd, tax_rate=args.tax_rate)
        if args.chart: plot_country_comparison(sector=args.sector, save_path=args.save_chart)
    elif args.cmd == "compare-sectors":
        compare_sectors(country=args.country, debt_ratio=args.debt_ratio, equity_ratio=1-args.debt_ratio, kd_pretax=args.kd, tax_rate=args.tax_rate)


if __name__ == "__main__":
    sys.exit(main())
