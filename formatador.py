import re

lists = []

with open('cnpj.txt','r', encoding='utf-8') as file:
    cnpj_list = file.readlines()
    
with open('cnpj_formatado.txt','w', encoding='utf-8') as file:
    for line in cnpj_list:
    # Remove characters '.', '-' e '/' with regular expressions
        linha = re.sub(r'[.\-\/]', '', line.strip())
    
        file.write(linha+"\n")


