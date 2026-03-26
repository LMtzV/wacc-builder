"""Charts for WACC visualization"""
import matplotlib.pyplot as plt
import numpy as np


def plot_waterfall(model, figsize=(10, 6), save_path=None):
    components = model.waterfall_components()
    labels = [c[0] for c in components]
    values = [c[1] for c in components]
    cum = [c[2] for c in components]
    colors = ["#008B8B", "#4682B4", "#000080", "#FFB90F", "#FFB90F"][:len(labels)]
    fig, ax = plt.subplots(figsize=figsize)
    rt = 0
    for i, (l, v, c) in enumerate(zip(labels, values, cum)):
        ax.bar(i, v, bottom=(0 if i==0 else rt), color=colors[i], edgecolor="black", width=0.6)
        ax.text(i, c+0.001, f"{c:.2%}", ha="center", va="bottom", fontsize=10, fontweight="bold")
        rt = c
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_ylabel("Cost of Equity"); ax.set_title(f"WACC Build-up: {model.sector} in {model.country}")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:>.1%}"))
    plt.tight_layout()
    if save_path: plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_country_comparison(sector="water_infrastructure", figsize=(12, 7), save_path=None):
    from wacc_builder.data import COUNTRY_RISK_PREMIUM
    from wacc_builder.model import WACCModel
    results = [(c, WACCModel(sector=sector, country=c).wacc) for c in COUNTRY_RISK_PREMIUM]
    results.sort(key=lambda x: x[1])
    labels, waccs = zip(*results)
    fig, ax = plt.subplots(figsize=figsize)
    colors = ["#2E8B57" if w<0.08 else "#4682B4" if w<0.12 else "#FF8C00" if w<0.16 else "#DC143C" for w in waccs]
    ax.barh(labels, waccs, color=colors, edgecolor="black")
    for i, (c, w) in enumerate(zip(labels, waccs)): ax.text(w+0.001, i, f"{w:.2%}", va="center")
    ax.set_title(f"WACC by Country: {sector}"); ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.1%}"))
    plt.tight_layout()
    if save_path: plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig
