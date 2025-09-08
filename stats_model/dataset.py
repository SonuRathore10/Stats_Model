from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from stats_model.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

import kagglehub  # Added for Kaggle download

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- DOWNLOAD DATASET FROM KAGGLE ----
    logger.info("Downloading dataset from Kaggle...")
    path = kagglehub.dataset_download(
        "mexwell/employee-performance-and-productivity-data",
        path=str(RAW_DATA_DIR)
    )
    logger.success(f"Dataset downloaded to: {path}")
    print("Path to dataset files:", path)
    # -------------------------------------


if __name__ == "__main__":
    app()