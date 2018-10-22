from models import * 
arquivo = None
try:
	arquivo = open ('perfis.csv', 'r')
	valores = arquivo.readline().split(':')
	Perfil(*valores)
	print('arquivo nao foi aberto')
	arquivo.close()

except (IOError, TypeError) as erro:
	print ('Deu erro')
#finally usado para executar codigo com ou sem erro
finally:
	if(arquivo is not None):
		print('fechando arquivo')
		arquivo.close()