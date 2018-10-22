# -*- coding: UTF-8 -*-
class Perfil(object):
	'Classe padrão para perfis de usuários' #opcional essa descrição
	# init é uma função construtora
	# cada um criado tem seu próprio self
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0	

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		#__ ai nao fica publico, nao existe encapsular, mas isso é como se fosse, esconde do mundo externo
		self.__curtidas += 1	

	#devolve o atributo que nao pode ser acessado pq n esta publico	
	def obter_curtidas(self):
		return self.__curtidas

	# @staticmethod	isso nao precisa colocar o self

	@classmethod #coloca a classe antes
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis	

#herança
class Perfil_Vip(Perfil):
	'Classe padrão para perfis de usuários' #opcional essa descrição
	# init é uma função construtora
	# cada um criado tem seu próprio self	

	def __init__ (self, nome, telefone, empresa,apelido='' ): #valor em branco
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		#herdar (nome da classe filha, e seu self)
		return super(Perfil_Vip, self).obter_curtidas() * 10.0





 # -*- coding: UTF-8 -*-
#class Pessoa(object):
#	'classe para calculo de imc' #opcional essa descrição
	# init é uma função construtora
	# cada um criado tem seu próprio self
#	def __init__(self, nome, peso, altura):
#		self.nome = nome
#		self.peso = peso
#		self.altura = altura	


#	def imprimir(self):
#		imc = self.peso/(self.altura * self.altura)
#		print 'IMC de %s: %s' % (self.nome, imc)




