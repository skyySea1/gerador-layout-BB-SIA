import re
from pathlib import Path
import pandas as pd

def extract_cnpjs_to_txt(dir_path: str,):
    
    dir_path= Path(dir_path)
    xls_files = dir_path.glob("*.xls")
    xlsx_files = dir_path.glob("*.xlsx")
    file_list = list(xls_files) + list(xlsx_files)
    
    cnpj_list = []
    
    for file in file_list:
        df = pd.read_excel(file, header=None, skiprows=10, usecols="A")
        cnpjs = df[0].dropna().astype(str).tolist() 
        cnpj_list.extend(cnpjs)
    with open("cnpj.txt", "w", encoding="utf-8") as file:
        for cnpj in cnpj_list:
            file.write(cnpj + "\n")
    return len(cnpj_list)  # Return the number of CNPJs extracted

def cnpj_format(in_file: str, out_file: str):
    with open(in_file, "r", encoding="utf-8") as input, \
    open(out_file, "w", encoding="utf-8") as output:
     for line in input:
    # Remove characters '.', '-' e '/' with regular expressions
        formatted_cnpj = re.sub(r'[.\-\/]', '', line.strip())
    
        output.write(formatted_cnpj+"\n")
          


extract_cnpjs_to_txt("cnpj")
cnpj_format("cnpj.txt", "cnpj_formatado.txt")
