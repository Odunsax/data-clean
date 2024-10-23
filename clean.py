import pandas as pd

# Load your data into a DataFrame
file_path = "your_file_path.csv"  # Update with your actual file path
df = pd.read_csv('clean.csv')

# Print the DataFrame structure
print("DataFrame Structure:")
print(df.info())

# List column names
print("Column Names:")
print(df.columns)

# Sample Data Cleaning

# Example: Changing data type of specific column, update 'Model Year' with actual column name
# Assuming you want to convert 'Model Year' (int) to a string as an example
if 'Model Year' in df.columns:
    df['Model Year'] = df['Model Year'].astype(str)
    print("Converted 'Model Year' column to string.")
else:
    print("'Model Year' column not found.")

# Example: Replacing incorrect values in the 'Make' column
if 'Make' in df.columns:
    df['Make'].replace('incorrect_value', 'correct_value', inplace=True)
    print("Replaced 'incorrect_value' with 'correct_value' in 'Make' column.")
else:
    print("'Make' column not found.")

# Example: Dropping rows with missing values in the 'Electric Range' column
if 'Electric Range' in df.columns:
    df.dropna(subset=['Electric Range'], inplace=True)
    print("Dropped rows with missing values in 'Electric Range' column.")
else:
    print("'Electric Range' column not found.")

# Saving the cleaned DataFrame
cleaned_file_path = "your_cleaned_file_path.csv"  # Update with your actual file path
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning completed and saved to:", cleaned_file_path)
