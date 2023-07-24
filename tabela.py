import tabula
# Duas formas de escrever o codigo de leitura de tabela em PDF
# Primeiro exemplo criar uma variavel para receber o arquivo pdf e depois passar a pagina que a variavel nova vai receber a tabela
pdf = 'C:\\Users\\rcomp\\Documents\\Python\\Arquivo_PDF.pdf'
tabela = tabula.read_pdf(pdf, pages = '6')
# Segundo exemplo criar uma variavel para receber o arquivo pdf e a pagina que contem a tabela
mytabela = tabula.read_pdf('C:\\Users\\rcomp\\Documents\\Python\\Arquivo_PDF.pdf', pages = '6')
print(tabela)
print(mytabela)