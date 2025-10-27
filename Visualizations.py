from healthcare_py import df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# ✅ Ensure numeric types for math/plots
# ----------------------------------------
numeric_cols = [
    "PSPS_NCH_PAYMENT_AMT", "PSPS_DENIED_SERVICES_CNT",
    "PSPS_SUBMITTED_SERVICE_CNT", "PSPS_ASSIGNED_SERVICES_CNT"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ----------------------------------------
# 1️⃣ Distribution of NCH Payment Amounts
# ----------------------------------------
plt.figure(figsize=(8, 5))
try:
    sns.histplot(df["PSPS_NCH_PAYMENT_AMT"].dropna(), bins=50, kde=True)
except AttributeError:
    sns.distplot(df["PSPS_NCH_PAYMENT_AMT"].dropna(), bins=50, kde=True, hist=True)

plt.title("Distribution of NCH Payment Amounts")
plt.xlabel("Payment Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ----------------------------------------
# 2️⃣ Top 10 Claim Types (TYPE_OF_SERVICE_CD)
# ----------------------------------------
top_types = df["TYPE_OF_SERVICE_CD"].value_counts().head(10)

plt.figure(figsize=(8, 5))
top_types.plot(kind='bar')
plt.title("Top 10 Claim Types")
plt.ylabel("Number of Claims")
plt.xlabel("Type of Service Code")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------------------
# 3️⃣ Rejection Rate by Region (PRICING_LOCALITY_CD)
# ----------------------------------------
region_grouped = df.groupby("PRICING_LOCALITY_CD")[
    ["PSPS_SUBMITTED_SERVICE_CNT", "PSPS_DENIED_SERVICES_CNT"]
].sum()

region_grouped["Rejection_Rate"] = (
    region_grouped["PSPS_DENIED_SERVICES_CNT"] / region_grouped["PSPS_SUBMITTED_SERVICE_CNT"]
)

plt.figure(figsize=(10, 6))
region_grouped["Rejection_Rate"].sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 Rejection Rates by Region")
plt.ylabel("Rejection Rate")
plt.xlabel("Pricing Locality Code")
plt.tight_layout()
plt.show()

# ----------------------------------------
# 4️⃣ Average Payment by BETOS Code
# ----------------------------------------
avg_payment_betos = df.groupby("HCPCS_BETOS_CD")["PSPS_NCH_PAYMENT_AMT"] \
                      .mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
avg_payment_betos.plot(kind='bar')
plt.title("Top 10 Avg Payment by BETOS Category")
plt.ylabel("Average Payment Amount")
plt.xlabel("BETOS Code")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
