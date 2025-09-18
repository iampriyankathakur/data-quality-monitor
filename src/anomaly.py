import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_outliers(df, numeric_cols):
    iso = IsolationForest(contamination=0.1, random_state=42)
    preds = iso.fit_predict(df[numeric_cols])
    outliers = (preds == -1).sum()
    return {"outliers_detected": int(outliers)}
