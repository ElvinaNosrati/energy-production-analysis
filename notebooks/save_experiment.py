from pathlib import Path
import torch

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