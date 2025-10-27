from healthcare_py import df
import pandas as pd

# Calculate average payment per assigned service
df["PSPS_ASSIGNED_SERVICES_CNT"] = pd.to_numeric(df["PSPS_ASSIGNED_SERVICES_CNT"], errors='coerce')
df["PSPS_NCH_PAYMENT_AMT"] = pd.to_numeric(df["PSPS_NCH_PAYMENT_AMT"], errors='coerce')

df_filtered = df[df["PSPS_ASSIGNED_SERVICES_CNT"] > 0].copy()
df_filtered["Payment_Per_Assigned_Service"] = (
    df_filtered["PSPS_NCH_PAYMENT_AMT"] / df_filtered["PSPS_ASSIGNED_SERVICES_CNT"]
)

avg_payment_per_service = df_filtered["Payment_Per_Assigned_Service"].mean()

# Summary
summary = """
Key Business Insights:

1. Top 5 providers account for a significant portion of total claim costs, indicating concentration of services.
2. BETOS categories reveal costlier service types, valuable for budgeting and audit focus.
3. Rejection rates vary significantly by region (pricing locality), indicating opportunities for provider training or policy review.
4. The average payment per assigned service is ${:.2f}, a good proxy for service-level efficiency and reimbursement quality.
5. Common claim types suggest where volume is concentrated—opportunities for optimization or automation.

""".format(avg_payment_per_service)

print(summary)
