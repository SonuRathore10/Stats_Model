# Stats_Model



RadhaKrishna

# Setup:
Run the `SetYouUp.ipynb` file to get started.

# Running the Project
0. Run `SetYouUp.ipynb`
1. Open the project folder in your terminal.
2. Start Jupyter Lab with `poetry run jupyter lab` or launch Visual Studio Code with `poetry run code .` (ensure VS Code is added to your system PATH to use the latter command).
3. If using VS Code, select the kernel that matches the project folder name.


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. 
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         stats_model and configuration for tools like black
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── stats_model   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes stats_model a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    └─── dataset.py              <- Scripts to download or generate data
```

--------

