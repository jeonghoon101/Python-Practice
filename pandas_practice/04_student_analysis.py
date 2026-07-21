from pathlib import Path

import pandas as pd

current_dir = Path(__file__).parent
csv_path = current_dir / "data" / "students.csv"

df = pd.read_csv(csv_path)

df = df.sort_values("Score", ascending=False)

print("=== Top 3 Students ===")
print(df.head(3))

print("\nSaved to students_result.csv")
df["Bonus"] = df["Score"] + 5
df.to_csv(current_dir / "data" / "students_result.csv", index=False)