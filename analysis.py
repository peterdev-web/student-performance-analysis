import pandas as pd

data = pd.read_csv("students.csv")

data["Average"] = data[["Math","English","Science"]].mean(axis=1)

top_student = data.loc[data["Average"].idxmax()]
lowest_student = data.loc[data["Average"].idxmin()]

print("Top student:", top_student["Name"], top_student["Average"])
print("Lowest student:", lowest_student["Name"], lowest_student["Average"])

print("\nClass average:", data["Average"].mean())

data.to_csv("results.csv", index=False)
