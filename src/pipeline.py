import argparse, pandas as pd
from checks import check_missing, check_duplicates
from anomaly import detect_outliers
from report import generate_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to dataset CSV")
    args = parser.parse_args()

    df = pd.read_csv(args.file)

    results = {}
    results["missing_values"] = check_missing(df)
    results["duplicates"] = check_duplicates(df)
    results["outliers"] = detect_outliers(df, df.select_dtypes("number").columns)

    report_path = generate_report(results)
    print(f"✅ Data Health Report saved at {report_path}")
