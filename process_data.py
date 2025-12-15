import pandas as pd
import os

data_folder = os.path.join(os.getcwd(), "data")
csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]

processed_dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    
    df.columns = df.columns.str.strip().str.lower()
    
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    df = df.dropna(subset=['product', 'quantity', 'price', 'date', 'region'])
    
    df = df[df['product'].str.strip().str.lower() == 'pink morsel']
    
    df['sales'] = df['quantity'] * df['price']
    
    df = df[['sales', 'date', 'region']]
    
    processed_dfs.append(df)

final_df = pd.concat(processed_dfs, ignore_index=True)

output_file = os.path.join(os.getcwd(), "formatted_sales.csv")
final_df.to_csv(output_file, index=False)

print(f"Formatted CSV saved successfully to {output_file}")
print(f"Number of rows in final CSV: {len(final_df)}")
