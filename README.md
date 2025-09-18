# 🧹 AI-Powered Data Quality Monitor

This toolkit evaluates datasets for **quality issues** and generates a **Data Health Report**.  
It checks for missing values, duplicates, anomalies, and schema drift to ensure **trustworthy AI pipelines**.


## 🚀 Features
- Missing value analysis
- Duplicate detection
- Outlier detection (Isolation Forest)
- Schema drift detection
- Markdown/HTML report output


## ⚙️ Installation
```bash
git clone https://github.com/yourusername/data-quality-monitor.git
cd data-quality-monitor
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python src/pipeline.py --file data/sample_dataset.csv

```

Output:

📄 reports/data_health_report.md (summary of checks)

📊 Charts of missing values & anomalies

## 📊 Tech Stack

Python

Data Validation: pandas, Great Expectations

Anomaly Detection: scikit-learn (Isolation Forest)

Visualization: matplotlib, seaborn

## 📌 Roadmap

 Add Streamlit dashboard

 Integrate drift detection for time-series

 Add alerting (Slack/Email)


 ⚙️ Requirements 
```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
great_expectations
pytest
```
