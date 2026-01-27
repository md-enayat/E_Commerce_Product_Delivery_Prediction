"""
Project Configuration and Paths
"""

from pathlib import Path

# --------------------------------------------------
# Project root (parent of src)
# --------------------------------------------------
BASE_DIR: Path = Path(__file__).resolve().parents[1]

# --------------------------------------------------
# Data paths
# --------------------------------------------------
DATA_DIR: Path = BASE_DIR / 'data'
DATA_FILE: Path = DATA_DIR / 'e_commerce_cleaned.csv'

# --------------------------------------------------
# Model paths
# --------------------------------------------------
MODEL_DIR: Path = BASE_DIR / 'models'
BEST_MODEL_PATH: Path = MODEL_DIR / 'best_model.joblib'
FEATURES_PATH: Path = MODEL_DIR / 'feature_list.json'

# --------------------------------------------------
# Target column
# --------------------------------------------------
TARGET_COL: str = 'Reached.on.Time_Y.N'

# --------------------------------------------------
# Train / Test & CV settings
# --------------------------------------------------
TEST_SIZE: float = 0.2
RANDOM_STATE: int = 42
CV_FOLDS: int = 5
N_JOBS: int = -1

# --------------------------------------------------
# Evaluation Metrics (CONFIG-DRIVEN)
# --------------------------------------------------

# Metric used during cross-validation / model selection
SCORING: str = 'f1'

# Metrics to report after final evaluation
EVALUATION_METRICS = [
    'accuracy',          # Required
    'confusion_matrix',  # Required
    'classification',    # Required (classification report)
    'roc_auc'            # Extra (recommended)
]
