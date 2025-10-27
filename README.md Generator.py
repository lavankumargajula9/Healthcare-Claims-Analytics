from healthcare_py import df
from Business_Insights_Summary import summary
readme = f"""
# Healthcare Claims Analytics

## 📌 Project Overview
This project performs an end-to-end analysis of a healthcare claims dataset to uncover patterns in provider billing, claim rejections, diagnosis cost, and payment delays.

## 📂 Dataset
- File: CMS_Healthcare.csv
- Records: {df.shape[0]}
- Features: {df.shape[1]}

## ⚙️ Tools Used
- Python (Pandas, NumPy)
- Visualization: Matplotlib, Seaborn, Plotly
- Jupyter Notebooks / .py scripts

## 📊 Key Analyses
- Top providers by total claims
- Diagnosis vs. average cost
- Rejection rates by region
- Monthly trend of claims
- Average payment time

## 📈 Visuals
- Trend of claim amount over time
- Cost distribution
- Claim type distribution
- Rejection heatmap by region

## ✅ Insights
{summary}

## 🚀 How to Run
1. Place `CMS_Healthcare.csv` in your working directory.
2. Run the notebook or script.
3. View results and modify for your business context.

---
"""

# Save to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)


print("README.md generated.")
