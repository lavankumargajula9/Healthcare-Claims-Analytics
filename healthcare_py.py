# Install packages if not already installed (uncomment below)
# !pip install pandas numpy matplotlib seaborn plotly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Load your dataset
df = pd.read_csv("C:\\Users\\Lavan\\Downloads\\CMS_Healthcare.csv")

# Display basic info
print(df.shape)
print(df.columns)
df.head()
