# print_all_codes_in_directory

- Objetivo: Script que lê de forma recursiva todos os arquivos dentro de uma pasta (inclusive suas subpastas), independente do formato, junta todos os textos e códigos e salva em formato ".txt". Indica, no texto compilado, o início e fim de cada arquivo e o caminho relativo de cada arquivo em relação à pasta passada como argumento.

- Usos: 
	- \> python print_codes.py <nome_arquivo_saída> <caminho_pasta_alvo_do_processamento>

- Saída: Um arquivo, um em formato ".txt" na pasta em que o script estiver rodando.

- Informações adicionais: 
	
	- Esse script pode ser útil para produzir relatórios, pedidos de patente e de registro de software

- Observações:
	
	- O programa dará erro para arquivos de mídia e imagens. Os seguintes formatos já estão filtrados:
		- PNG, JPEG, JPG E ICO
	- Se houver outros formatos gerando erro na saída do programa, é necessário adicionar no "if" dentro da função.
	- Você pode usar o arquivo em .txt e abri-lo no Notepad++ ou outro editor para salvar como pdf. Não vale a pena uma aplicação em python que salve em pdf pelo fato de haver caracteres que não são triviais de converter, o índice de erros é muito altos.