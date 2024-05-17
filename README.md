## Merging & Changing the Format to Tabular

🤖 This Python script processes sales data from multiple Excel files, merges the data, and saves it in a consolidated format. It starts by defining file paths for the Excel files containing sales data for Norway, Spain, and Ireland. These files are read into separate DataFrames and then combined into a single DataFrame. The combined data is then transformed from a wide format to a long format using the melt function, which reshapes the DataFrame such that each row represents a unique combination of country, month, and sales value. The script extracts the month number from the column headers and converts it to an end-of-month date format, then reformats the dates into a 'DD/MM/YYYY' string format. The sales values are converted to numeric format, handling any non-numeric values, and are then formatted as currency without decimal places. Finally, the processed data is saved to a new Excel file named "Combined_Sales.xlsx". This script efficiently consolidates and standardizes sales data across multiple countries into a single, easy-to-analyze file.





