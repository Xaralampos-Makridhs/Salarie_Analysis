# Salarie_Analysis

This project analyzes salary data by reading an Excel table of salary classes and the number of people in each class, then computes key statistics and visualizations. The workflow includes transforming the table with statistical calculations and producing a cumulative frequency chart.

---

## Workflow Overview

### 1. Input Table

Start with an Excel file (`salaries_table.xlsx`) containing the salary distribution:

| Salaries (€)   | People |
| -------------- | ------ |
| 700 - 1000     | 12     |
| 1000 - 1300    | 20     |
| 1300 - 1600    | 15     |
| 1600 - 1900    | 3      |

---

### 2. Table During and After Processing

After running the analysis scripts, new columns are added with computed statistics:

| Salaries (€)   | People | Relative Frequency | Cumulative Frequency | Cumulative Relative Frequency | Midpoint |
| -------------- | ------ | ----------------- | -------------------- | ----------------------------- | -------- |
| 700 - 1000     | 12     | 0.24              | 12                   | 0.24                          | 850      |
| 1000 - 1300    | 20     | 0.40              | 32                   | 0.64                          | 1150     |
| 1300 - 1600    | 15     | 0.30              | 47                   | 0.94                          | 1450     |
| 1600 - 1900    | 3      | 0.06              | 50                   | 1.00                          | 1750     |
| **Total**      | 50     |                   | 50                   | 1.00                          |          |

---

### 3. Cumulative Frequency Chart

The script generates a cumulative frequency line chart visualizing the salary distribution:

<img width="1919" height="1017" alt="cumulativechart" src="https://github.com/user-attachments/assets/e6fa9888-6889-41ad-927d-de91cef21bb6" />


---

## Features

- Reads and processes salary class data from Excel
- Computes:
  - Relative Frequency
  - Cumulative Frequency
  - Cumulative Relative Frequency
  - Salary class midpoints
  - Mean, median, and mode for the salary data
- Updates the Excel file with new statistical columns
- Generates a cumulative frequency chart for visualization

---

## Code Documentation

Every method and line of code in the repository is thoroughly commented to explain its purpose and logic. This makes the project easy to understand and modify, even for users with limited experience in Python or data analysis.

---

## Technologies Used

- Python
- pandas
- matplotlib
- Excel (.xlsx format)

4. **Review results:**
   - Updated Excel file with additional columns.
   - Cumulative frequency chart displayed.
   - Mean, median, and mode shown in the console.

---

## License

This project is licensed under the MIT License.

## Proccess Print Screens

<img width="369" height="154" alt="printscreentable" src="https://github.com/user-attachments/assets/fa9f356c-c3c4-4f08-b17b-87764b756c04" />

<img width="350" height="268" alt="exceltable" src="https://github.com/user-attachments/assets/7b07178c-3878-4955-89da-b3146ab417fb" />


<img width="565" height="165" alt="table" src="https://github.com/user-attachments/assets/0f187166-1c3f-4d1b-b55c-f854966c5f6c" />


<img width="657" height="192" alt="mode_median_mean" src="https://github.com/user-attachments/assets/29d7580a-a846-47ef-a381-1703b6a4d28f" />

