import pandas as pd

# File paths
file_paths = ["Norway.xlsx", "Spain.xlsx", "Ireland.xlsx"]
output_file = "Combined_Sales.xlsx"  # Output file path

# Read and combine Excel files
dataframes = [pd.read_excel(file) for file in file_paths]
merged_data = pd.concat(dataframes, ignore_index=True)

# Melt the dataframe to convert it to tabular format
melted_data = pd.melt(merged_data, id_vars=[
                      'Country'], var_name='Month', value_name='Sales')

# Extract month number from the 'Month' column and convert to end of month format
melted_data['Month'] = pd.to_datetime(melted_data['Month'].str.extract(
    r'(\d+)')[0].astype(int).astype(str) + '/2024', format='%m/%Y') + pd.offsets.MonthEnd(1)

# Convert 'Month' column to string with the desired format (DD/MM/YYYY)
melted_data['Month'] = melted_data['Month'].dt.strftime('%d/%m/%Y')

# Convert 'Sales' column to numeric, handling non-numeric values
melted_data['Sales'] = pd.to_numeric(melted_data['Sales'], errors='coerce')

# Format 'Sales' column as currency without decimal places
melted_data['Sales'] = melted_data['Sales'].apply(
    lambda x: '${:,.0f}'.format(x))

# Save combined data to Excel file
melted_data.to_excel(output_file, index=False)

print("Combined data saved to", output_file)
