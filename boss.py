import camelot
import os
import pandas as pd

# Set the Ghostscript path
os.environ['PATH'] = r'C:\Program Files\gs\gs9.56.1\bin' + os.pathsep + os.environ['PATH']

# Specify the path to your PDF file
file_path = '1.pdf'

# Extract tables specifying the columns (approximate x-coordinates of the column edges in points)
tables = camelot.read_pdf(file_path, pages='all', flavor='lattice')

# Check the number of tables found
print(f"Number of tables found: {len(tables)}")


dfs = []

# Iterate through the tables and print the first few rows
for i, table in enumerate(tables):
    df = table.df

# Rename columns if needed (assuming the first row is the header)

    df = df.iloc[:, [1, 2, 3]]

    df.columns = ['Village / Town / City / Location', 'Region', 'State']
    df = df.drop(0).reset_index(drop=True)

    dfs.append(df)

final_df = pd.concat(dfs, ignore_index = True)

# Save the DataFrame to a CSV file if needed
final_df.to_csv('location_mapping.csv', index=False)
