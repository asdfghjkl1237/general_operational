import pandas as pd
import os

def get_all_file_paths(root_dir):
    file_paths = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

root_folder = ""
files = get_all_file_paths(root_folder)

for f in files:
    print(f)

for f in files:
    print(f)

    xlsx_file = f
    df = pd.read_excel(xlsx_file, dtype=str, keep_default_na=False, engine="openpyxl", sheet_name=None)
    
    for sheet, data in df.items():
        csv_file = '' # replace this
        data.to_csv(csv_file, index=False, encoding="utf-8")  # Save CSV with UTF-8 encoding
        print(f"Converted: {csv_file}")
