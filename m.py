import pandas as pd

# # Assuming your CSV data is in a file named "input.csv"
input_file = "mst-1.csv"

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(input_file)
# print(df['marks'])
# df['marks'] = pd.to_numeric(df['marks'], errors='coerce')
# # Create new columns 'co1', 'co2', and 'co3' with initial values as NaN
# df['co1'] = pd.Series(dtype=float)
# df['co2'] = pd.Series(dtype=float)
# df['co3'] = pd.Series(dtype=float)

# # Define the conditions for each column
# condition_co1 = df['marks'] < 7
# condition_co2 = (df['marks'] >= 7) & (df['marks'] < 14)
# condition_co3 = df['marks'] >= 14

# # Update the values in 'co1', 'co2', and 'co3' columns based on the conditions
# df.loc[condition_co1, 'co1'] = df.loc[condition_co1, 'marks']
# df.loc[condition_co2, 'co2'] = df.loc[condition_co2, 'marks']
# df.loc[condition_co3, 'co3'] = df.loc[condition_co3, 'marks']

# # Display the resulting DataFrame
# print(df)
import pandas as pd

# # Assuming your CSV data is in a file named "input.csv"
# input_file = "input.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Convert the "marks" column to numeric values
df['marks'] = pd.to_numeric(df['marks'], errors='coerce')

# Function to divide a number into three numbers
def divide_numbers(number):
    # Divide into three numbers
    number1 = min(number - 1, 7)  # First number less than 7
    number2 = min(number - number1 - 1, 7)  # Second number less than 7
    number3 = min(number - number1 - number2, 6)  # Third number less than 6
    return number1, number2, number3

# Apply the division function to each value in the "marks" column
df[['co1', 'co2', 'co3']] = df['marks'].apply(lambda x: pd.Series(divide_numbers(x)))

df.to_csv("mst-1-updated.csv")
# Display the resulting DataFrame
print(df)
