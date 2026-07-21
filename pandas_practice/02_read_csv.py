from pathlib import Path

import pandas as pd

current_dir = Path(__file__).parent
csv_path = current_dir / "data" / "students.csv"

df = pd.read_csv(csv_path)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
