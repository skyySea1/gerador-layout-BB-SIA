from datetime import datetime

data_atual = datetime.now().strftime("%Y%m%d")

# comporsição da estrutura do header, detalhes e trailer
campos_header = [
{"identificador_header" : "0"},
{"data": data_atual},
{"nome_arquivo": "GFAF035E"},
{"mci_org" :""}] # Insira o mci do seu orgão

campos_detalhe= [
 {"identificador_detalhe" : "1"},
 {"data": data_atual},
 {"cnpj": ""}, # essa chava sera reestruturada para iterar sob os cnpjs
 {"mci_org" :""}]

# como o valor é fixo, é mais prático definir, ao invés de inferir
zeros_redundantes_header= 34
zeros_redundantes_detalhe=35
zeros_redundantes_trailer=50
trailer="9000007940" # os últimos 4 números devem conter a quantidade de registros incluindo o header e trailer

with open("cnpj_formatado1.txt", "r") as file:
    cnpj_lines = file.readlines()
    
def formatar_header():    
    header_concat = "".join([var for campo in campos_header for var in campo.values()])
    header_f= header_concat.ljust(60, " ")
    return header_f
    
#recriar a dictlist
def formatar_registro(cnpj):
 campos_detalhe= [
 {"identificador_detalhe" : "1"},
 {"data": data_atual},
 {"cnpj": cnpj.strip()+"S"},
 {"mci_" :""}]
 registro_concat= "".join([var for campo in campos_detalhe for var in campo.values()])
 registro_f = registro_concat.ljust(60, " ")
 return registro_f

detalhe_f= ""

header = formatar_header()
registros = [formatar_registro(cnpj) for cnpj in cnpj_lines ]

def gerar_layout():
    with open("layout.txt","w", encoding="utf-8") as layout:
        layout.write(header + "\n")
        for i in registros:
            layout.write(i +"\n")
        layout.write(trailer.ljust(60, " "))

gerar_layout()


