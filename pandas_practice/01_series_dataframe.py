import pandas as pd

scores = pd.Series([90, 80, 95, 100])
print(scores)

fruits = pd.Series(["Apple", "Banana", "Orange"])
print(fruits)

student = {
    "Name": ["Kim", "Lee", "Park"],
    "Age": [23, 22, 24],
    "Score": [90, 80, 95]
}
df = pd.DataFrame(student)
print(df)
print(df["Name"])
print(df[["Name", "Score"]])
print(df.loc[0])
print(df.iloc[1])
print(df[df["Score"] >= 90])
print(df[(df["Score"] >= 90) & (df["Age"] >= 23)])
df.loc[1, "Score"] = 100
print(df)
df["Pass"] = True
print(df)
df["Bonus"] = df["Score"] + 5
print(df)