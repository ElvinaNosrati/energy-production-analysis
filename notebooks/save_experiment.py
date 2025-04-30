from pathlib import Path
import pandas as pd
import torch
import os
import joblib

def save_experiment(
    station: str,
    model_name: str,
    net: torch.nn.Module,
    metrics_df,
    train_figs: dict,
    pred_figs: dict,
    base_dir: Path = Path("..")
):
    station_dir = base_dir / station / model_name
    model_dir = station_dir / "model"
    figures_dir = station_dir / "figures"
    predictions_dir = station_dir / "predictions"
    
    for folder in [model_dir, figures_dir, predictions_dir]:
        folder.mkdir(parents=True, exist_ok=True)
    
    torch.save(net.state_dict(), model_dir / f"{model_name}.pt")
    torch.save(net, model_dir / f"{model_name}.pth")
    
    metrics_df.to_csv(station_dir / "metrics.csv", index=False)
    
    for name, fig in train_figs.items():
        fig.savefig(figures_dir / f"{name}.png", dpi=150, bbox_inches='tight')

    
    for name, fig in pred_figs.items():
        fig.savefig(predictions_dir / f"{name}.png", dpi=150)


def save_ml_experiment(
    station: str,
    results: dict,
    y_test,
    metrics_df: pd.DataFrame,
    table_fig,
    barplot_fig,
    pred_figs: dict, 
    models_dict: dict,
    base_dir: Path = Path("..")
):
    for model_name in models_dict:
        station_model_dir = base_dir / station / model_name
        model_dir = station_model_dir / "model"
        figures_dir = station_model_dir / "figures"
        predictions_dir = station_model_dir / "predictions"

        for folder in [station_model_dir, model_dir, figures_dir, predictions_dir]:
            folder.mkdir(parents=True, exist_ok=True)

        metrics_df.to_csv(station_model_dir / "metrics.csv", index=False)

        table_fig.savefig(figures_dir / "metrics_table.png", dpi=150, bbox_inches='tight')
        barplot_fig.savefig(figures_dir / "metrics_barplot.png", dpi=150, bbox_inches='tight')

        if "AllModels" in pred_figs:
            pred_figs["AllModels"].savefig(predictions_dir / "all_models.png", dpi=150, bbox_inches='tight')

        joblib.dump(models_dict[model_name], model_dir / f"{model_name}.joblib")
