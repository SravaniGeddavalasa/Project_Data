import pandas as pd

# ASSIGNMENT: CLEAN A MESSY DATASET USING PANDAS

# 1. LOAD THE CSV FILE
df = pd.read_csv("data.csv")
print("First 5 Rows:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nDataset Shape:")
print(df.shape)

# 2. CHECK MISSING VALUES
print("\nMissing Values:")
print(df.isnull().sum())

# 3. HANDLE MISSING VALUES
# Fill missing Calories with the average Calories
df["Calories"] = df["Calories"].fillna(df["Calories"].mean())
# Fill missing Date using the previous available date
df["Date"] = df["Date"].ffill()
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 4. REMOVE DUPLICATE ROWS
print("\nDuplicate Rows Before Removing:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate Rows After Removing:")
print(df.duplicated().sum())

# 5. FILTER ROWS
# Select rows where Pulse is greater than 100
filtered_data = df[df["Pulse"] > 100]
print("\nRows Where Pulse is Greater Than 100:")
print(filtered_data)

# 6. CREATE A NEW COLUMN
# Calculate calories burned per minute
df["Calories_per_Minute"] = df["Calories"] / df["Duration"]
print("\nDataset After Creating New Column:")
print(df)


# 7. SAVE THE CLEANED DATASET
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset saved successfully as cleaned_data.csv")