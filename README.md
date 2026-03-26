# wacc-builder

A Python CLI tool for building WACC from first principles using CAPM + CRP for emerging market infrastructure projects.

## Methodology

WACC = Ke × (E/V) + Kd * (1-T) * (D/V)

Ke = Rf + βL × ERP + CRP + Premiums

Hamada: βL = βU × [1 + (1-T) × (D/E)]

## Install

```bash
pip install -e .
```

## Usage

```bash
wacc-build --sector water_infrastructure --country MX --debt-ratio 0.65
wacc-compare-countries --sector water_infrastructure
wacc-compare-sectors --country MX
```

```python
from wacc_builder.model import WACCModel
model = WACCModel(sector="water_infrastructure", country="MX", debt_ratio=0.65)
model.print_summary()
```

## License
MIT
