from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import requests

from stats_model.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()
import os
os.system('poetry update')
os.system('poetry install')
os.system('poetry lock')


# Get the absolute path to the project root
project_root = Path(__file__).resolve().parent.parent
processed_dir = project_root / 'data' / 'processed'
processed_dir.mkdir(parents=True, exist_ok=True)
def download_from_gdrive(gdrive_url: str, dest_path: Path):
    """
    Download a file from a Google Drive shareable link.
    """
    import re

    # Ensure the destination directory exists
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Extract file ID from the Google Drive URL
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', gdrive_url)
    if not match:
        raise ValueError("Invalid Google Drive URL format.")
    file_id = match.group(1)
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    logger.info(f"Downloading from Google Drive: {gdrive_url}")
    response = requests.get(download_url, stream=True)
    response.raise_for_status()

    with open(dest_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192), desc="Downloading", unit="B", unit_scale=True):
            if chunk:
                f.write(chunk)
    logger.success(f"File downloaded to: {dest_path}")

@app.command()

def main(
    input_path: Path = RAW_DATA_DIR / "Life_Expectancy_Data.csv",
    output_path: Path = PROCESSED_DATA_DIR / "Life_Expectancy_Data.csv",
):
    # ---- DOWNLOAD DATASET FROM GOOGLE DRIVE ----
    gdrive_url = "https://drive.google.com/file/d/1WliKENZpN40X5VckKajTyBQdRwq3oNuk/view?usp=sharing"
    dest_path = RAW_DATA_DIR / "Life_Expectancy_Data.csv"
    download_from_gdrive(gdrive_url, dest_path)
    print("Path to dataset file:", dest_path)
    # --------------------------------------------

if __name__ == "__main__":
    app()