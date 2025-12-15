import pandas as pd
import os

data_folder = os.path.join(os.getcwd(), "data")
csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]

processed_dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Remove $ sign from price and convert to float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Convert quantity to numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    # Drop rows with missing critical data
    df = df.dropna(subset=['product', 'quantity', 'price', 'date', 'region'])
    
    # Filter for Pink Morsels (case-insensitive, strip spaces)
    df = df[df['product'].str.strip().str.lower() == 'pink morsel']
    
    # Calculate sales
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only required columns
    df = df[['sales', 'date', 'region']]
    
    processed_dfs.append(df)

# Combine all files
final_df = pd.concat(processed_dfs, ignore_index=True)

# Save to CSV
output_file = os.path.join(os.getcwd(), "formatted_sales.csv")
final_df.to_csv(output_file, index=False)

print(f"Formatted CSV saved successfully to {output_file}")
print(f"Number of rows in final CSV: {len(final_df)}")
