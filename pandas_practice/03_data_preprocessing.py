from pathlib import Path

import pandas as pd

current_dir = Path(__file__).parent
csv_path = current_dir / "data" / "students.csv"

df = pd.read_csv(csv_path)

print(df.sort_values("Score"))
print(df.sort_values("Score", ascending=False))

dup = {
    "Name":["Kim","Kim","Lee","Park"],
    "Score":[90,90,80,95]
}

df1 = pd.DataFrame(dup)
print(df1)
print(df1.drop_duplicates())

student = {
    "Name": ["Kim", "Lee", "Park"],
    "Age": [23, None, 24],
    "Score": [90, 80, None]
}

df2 = pd.DataFrame(student)

print(df2)
print(df2.dropna())
print(df2.fillna(0))
print(df2.fillna(df2["Age"].mean()))

df["Score"] += 5
df.to_csv(current_dir / "data" / "students_updated.csv", index=False)
