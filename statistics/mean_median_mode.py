import pandas as pd
from statistics import mode

# Path to the Excel file with salary data
file_path = 'salaries_table.xlsx'

# Read Excel file
df = pd.read_excel(file_path)

# Remove 'Total' row if it exists
df = df[df['Salaries (€)'] != 'Total']

# Function to calculate midpoint of each salary class
def class_midpoint(salary_range):
    lower, upper = salary_range.split('-')
    return (float(lower) + float(upper)) / 2

# Calculate midpoints
df['Midpoint'] = df['Salaries (€)'].apply(class_midpoint)

# 1. Mean 
mean_salary = (df['Midpoint'] * df['People']).sum() / df['People'].sum()

# 2. Create full salary list to calculate median and mode
salary_list = []
for _, row in df.iterrows():
    salary_list.extend([row['Midpoint']] * row['People'])

# 2. Median 
median_salary = pd.Series(salary_list).median()

# 3. Mode 
mode_salary = pd.Series(salary_list).mode()[0]

# Print results
print(f"Mean salary: {mean_salary:.2f} €")
print(f"Median salary: {median_salary:.2f} €")
print(f"Mode salary: {mode_salary:.2f} €")

df.to_excel("salaries_table.xlsx", index=False)