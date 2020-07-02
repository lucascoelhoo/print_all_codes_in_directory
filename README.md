# print_pdf_all_codes_in_directory

- Objetivo: Script que lê de forma recursiva todos os arquivos dentro de uma pasta (inclusive suas subpastas), independente do formato, junta todos os textos e códigos e salva em formato ".pdf" e ".txt". Indica, no texto compilado, o início e fim de cada arquivo e o caminho relativo de cada arquivo em relação à pasta passada como argumento.

- Usos: 
	- \> python print_codes.py <nome_arquivo_saída> <caminho_pasta_alvo_do_processamento>

- Saída: Dois arquivos, um em formato ".pdf" e outro em formato ".txt" na pasta em que o script estiver rodando.

- Informações adicionais: 
	
	- Caso deseje mudar a fonte, a quantidade de caracteres na divisão dos arquivos, estilos, etc, edite a parte indicada no código.
	- Esse script pode ser útil para produzir relatórios, pedidos de patente e de registro de software
