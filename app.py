# -*- coding: UTF-8 -*-

def listar(nomes):
	print 'Listando Nomes:'
	for nome in nomes:
		print nome

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)


def remover(nomes):
	print 'Qual nome você gostaria de remover?'
	remover_nome = raw_input()
	nomes.remove(remover_nome)


def alterar(nomes):
	print 'Qual nome você gostaria de alterar?'
	nome_vai_alterar = raw_input()
	resposta = nome_vai_alterar in nomes
	if(resposta):
		print 'Digite novo nome que quer colocar:'
		novo_nome = raw_input()
		indice = nomes.index(nome_vai_alterar)
		nomes[indice] = novo_nome
	else:
		print 'Esse nome nao esta cadastrado'

def procurar(nomes):
	print 'Digite nome a procurar'
	nome_procurar = raw_input()
	resposta = nome_procurar in nomes
	if(resposta):
		print 'Nome está na lista'

	else:
		print 'Nome não está na lista'

def procurar_regex(nomes):
	import re
	print('Digite a expressao regular')
	regex = raw_input()
	nomes_concatenados = ''.join(nomes)
	resultados = re.findall(regex, nomes_concatenados)
	print(resultados)


def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'): 
		print 'Digite:'
		print'1 para cadastrar, 0 para terminar, '
		print'2 para listar nomes, 3 para remover nome da lista'
		print'4 para alterar um nome da lista'
		print'5 para procurar nome na lista'
		print'6 procurar regex'
		escolha = raw_input()
		if(escolha == '1'):
			cadastrar(nomes)
		if(escolha == '2'):
			listar(nomes)
		if(escolha == '3'):
			remover(nomes)
		if(escolha == '4'):
			alterar(nomes)
		if(escolha == '5'):
			procurar(nomes)
		if(escolha == '6'):
			procurar_regex(nomes)
	

menu()
