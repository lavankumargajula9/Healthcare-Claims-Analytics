from healthcare_py import df

# 1️⃣ Average Cost per Diagnosis (using HCPCS_BETOS_CD as proxy for diagnosis)
avg_cost_betos = df.groupby("HCPCS_BETOS_CD")["PSPS_NCH_PAYMENT_AMT"] \
                   .mean().sort_values(ascending=False)

print("=== Average NCH Payment per BETOS Category ===")
print(avg_cost_betos.head(10))
print()

# 2️⃣ Rejection Rate by Region (using PRICING_LOCALITY_CD)
region_grouped = df.groupby("PRICING_LOCALITY_CD")[
    ["PSPS_SUBMITTED_SERVICE_CNT", "PSPS_DENIED_SERVICES_CNT"]
].sum()

region_grouped["Rejection_Rate"] = (
    region_grouped["PSPS_DENIED_SERVICES_CNT"] / region_grouped["PSPS_SUBMITTED_SERVICE_CNT"]
)

print("=== Rejection Rate by Pricing Locality Code ===")
print(region_grouped["Rejection_Rate"].sort_values(ascending=False))
print()

# 3️⃣ Average Payment Per Assigned Service
df_filtered = df[df["PSPS_ASSIGNED_SERVICES_CNT"] > 0].copy()

df_filtered["Payment_Per_Assigned_Service"] = (
    df_filtered["PSPS_NCH_PAYMENT_AMT"] / df_filtered["PSPS_ASSIGNED_SERVICES_CNT"]
)

avg_payment = df_filtered["Payment_Per_Assigned_Service"].mean()
print("=== Average Payment per Assigned Service ===")
print(round(avg_payment, 2))
print()

# 4️⃣ Top Claim Types (TYPE_OF_SERVICE_CD)
top_claim_types = df["TYPE_OF_SERVICE_CD"].value_counts().head(5)

print("=== Top Claim Types ===")
print(top_claim_types)
print()

# 5️⃣ Top Providers by Total Claim Amount (CARRIER_NUM)
top_providers = df.groupby("CARRIER_NUM")["PSPS_NCH_PAYMENT_AMT"] \
                  .sum().sort_values(ascending=False).head(5)

print("=== Top 5 Providers by NCH Payment Amount ===")
print(top_providers)
print()

# 6️⃣ Most Expensive Procedures (based on HCPCS_CD average cost)
expensive_procedures = df.groupby("HCPCS_CD")["PSPS_NCH_PAYMENT_AMT"] \
                         .mean().sort_values(ascending=False).head(10)

print("=== Top 10 Most Expensive Procedures (Avg NCH Payment) ===")
print(expensive_procedures)
print()
