def processa_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final - 4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial:posicao_final]
	return 'Enviando convite para %s %s' %(parte1, parte2)
