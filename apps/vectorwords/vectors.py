
#Importação do minceamet disponibilizado no link: https://github.com/michaelfairley/mincemeatpy
import mincemeat
import glob
import csv

#Realiza o agrupamento dos arquivos adicionados pela API
text_files = glob.glob('C:\\Users\\hac027\\Documents\\GitHub\\WordsVector\\media\\*')

def file_contents(file_name):
	f=open(file_name)
	try:
		return f.read()
	finally:
		f.close

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def mapfn(k, v):
	print('map ' + k)
	from stopwords import allStopWords
	for line in v.splitlines():
		for word in line.split():
			if (word not in allStopWords ):
				yield word, 1

def reducefn(k, v):
	print('reduce ' + k)
	return sum(v)


s = mincemeat.Server()


#A fonte de dados pode ser qualquer objeto do tipo dicionário
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")


#Cria o documento com o resultado das palavras
w = csv.writer(open("C:\\Users\\hac027\\Documents\\GitHub\\WordsVector\\media\\RESULT.csv", "w"))
for k, v in results.items():
	w.writerow([k, v])
