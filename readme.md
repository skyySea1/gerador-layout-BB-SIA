# ESTRUTURA 

**Regras:**     
- todos os campos devem ter 60 posições, portanto 
- preciso adicionar 0's a direita para preencher o restante que não for o registro

*Campos*

Header
| data no formato AAAAMMDD
- ``0+data+nomePadrão+MCI+filler``
- header: 0+20250313+GFAF035E+MCI+0 * filler restante

Detalhe(registros desejados)
- ``1+MCI+CNPJ+SouN+filler``


**HEADER:** ``020250313GFAF035E+MCI``
/ 26 linhas válidas

**REGISTROS:**
Linhas contendo cada registro para cada cnpj (registro/detalhe) / 25 linhas válidas


 **TRAILER:** ``9000004027`` / substituir os 0's pela quantidade de registros incluindo o trailer e header / o trailer possuí apenas 10 linhas válidas


Ressalvas:
- preferi tornar o código mais acessível pra reuso documentando e usando uma abordagem mais flexível, pensei em usar programação funcional, mas é detalhe.
- adicionei um módulo que obtém a data atual automaticamente para fins de para reuso
- caso o programa vá ser usado por mais pessoas em breve, pode ser conveniente montar um script gráfico onde vc adiciona a lista de cnpjs em um campo, o programa formata e adiciona automaticamente os valores e gera o layout pronto