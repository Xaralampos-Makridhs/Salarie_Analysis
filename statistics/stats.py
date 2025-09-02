import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for plotting

file_path = 'salaries_table.xlsx'  # Path to the Excel file
df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame

# Remove the row labeled 'Total' if it exists
df = df[df['Salaries (€)'] != 'Total']

# Calculate total number of people
total_people = df['People'].sum()

# Compute relative frequency of each salary class
df['Relative Frequency'] = df['People'] / total_people

# Compute cumulative frequency
df['Cumulative Frequency'] = df['People'].cumsum()

# Compute cumulative relative frequency
df['Cumulative Relative Frequency'] = df['Cumulative Frequency'] / total_people

# Add a 'Total' row showing the total number of people
total_row = {
    "Salaries (€)": "Total",
    "People": total_people
    # Other columns remain empty
}

df = pd.concat([df, pd.DataFrame([total_row])], ignore_index=True)  # Append the total row to the DataFrame

print(df) #Prints Excel table

#Save the updates
df.to_excel(file_path, index=False)

# Plot cumulative frequency line chart
plt.figure(figsize=(8,5))  # Set figure size
plt.plot(df['Salaries (€)'], df['Cumulative Frequency'], marker='o', linestyle='-', color='blue')  # Plot line with markers
plt.xlabel('Salary Classes')  # X-axis label
plt.ylabel('Cumulative Frequency')  # Y-axis label
plt.title('Cumulative Frequency Line Chart by Salary Class')  # Chart title
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)  # Show grid
plt.tight_layout()  # Adjust layout to prevent overlap

plt.show()  # Display the plot
