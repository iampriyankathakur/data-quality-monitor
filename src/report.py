import json

def generate_report(results, output_path="reports/data_health_report.md"):
    with open(output_path, "w") as f:
        f.write("# 🧹 Data Health Report\n\n")
        f.write("## Summary\n")
        f.write("```json\n")
        f.write(json.dumps(results, indent=2))
        f.write("\n```")
    return output_path
