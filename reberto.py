#reberto.py agora vai jogar campo minado otarios
from dataclasses import dataclass
import sys

@dataclass
class Tno_ad:
	cell: (int,int)
	f: float = -1

#checa se a casa pertence ao tabuleiro
def valido(x, y) :
    if (x < 0 or x > 9 or
        y < 0 or y > 9) :
        return False
    return True

#checa todos os vizinhos
def checkNeighbors(mapa, x, y):
	for a in range(x-1, x+1):
		for b in range(y-1, y+1):
			if(valido(a,b)):
				if(mapa[a][b]== ' '):
					return 1
	return 0

def contarCasas(mapa):
	x = 0
	for linha in mapa:
		for cell in linha:
			if cell != " ";
				x+=1
	return x

#gera a lista de nós abertos e fechados
def gerarListas(mapa, abertos, fechados):
	x=0
	for linha in mapa:
		y=0
		for cell in linha:
			if(cell=='F'):
				fechados.append((x,y))
			elif(cell==0):
				fechados.append((x,y))
			elif(cell!=0 and cell!=' ' and cell!='F'):
				if(checkNeighbors(mapa,x,y)==1):
					abertos.append((x,y))
				else:
					fechados.append((x,y))
			y=y+1
		x=x+1

def checarCasa(mapa, cell):
	casasFechadas == 0
	bombas = 0
	x,y = cell
	for a in range(x-1, x+1):
		for b in range(y-1, y+1):
			if(valido(a,b)):
				if(mapa[a][b]== ' '):
					casasFechadas+= 1
				elif(mapa[a][b] == 'F'):
					bombas += 1

	return (int(mapa[x][y]) - bombas)/ casasFechadas


def casasAAbrir(mapa, cell):
	linha, coluna = cell
	casasFechadas = 0
	for a in range(linha-1, linha+1):
		for b in range(coluna-1, coluna+1):
			if(valido(a,b))
				if(mapa[a][b] == ' '):
					casasFechadas+= 1

	return casasFechadas


def funcHeurisitca(mapa,cell):
	return casasAAbrir(mapa,cell) + contarCasas(mapa)


def econtrarBombas(mapa):
	from minesweeper import *
	vizinhos = []
	probRedor = []
	bombas = []
	x = 0
	for linha in mapa:
		y = 0
		for cell in linha:
			if cell == " ":
				vizinhos = getneighbors(mapa,x,y)
				for v in vizinhos:
					if v != " ":
						probRedor.append(checarCasa(mapa,v))
				if max(probRedor) == 1:
					bombas.append(x,y)
			y+=1
		x+=1

	return bombas


def aEstrelaBusca(mapa):
	abertos=[]
	fechados=[]
	
	#while True:
	gerarListas(mapa, abertos, fechados)
	temp = 0
	val = 0
	cellAbrir = (4,4)
	if casasAAbrir(mapa) == 0:
		#break
		return (-1,-1)

	if not abertos:
		for cell in abertos:
			temp = funcHeurisitca(mapa,cell)
			if(temp > val):
				cellAbrir = cell
				val = temp

	return cellAbrir









'''
#checar ao redor
def checarCasa(cell, mapa, numero):
	linha, coluna = cell
	t = Tno_ad(cell)
	print(t)
	casasFechadas = 0
	if (0 < linha < 8) and (0 < coluna < 8):
		for x in [(linha-1), linha, (linha+1)]:
			for y in [coluna-1, coluna, coluna+1]:
				if mapa[x][y] == ' ': #ciaxa estiver fechada
					casasFechadas+= 1
				elif mapa[x][y] == 'F':#caixa que estiver marcada
					casasFechadas-=1

	elif (linha == 0) and (0 < coluna < 8):
			for x in [linha, linha+1]:
				for y in [coluna-1, coluna, coluna+1]:
					if mapa[x][y] == ' ': #ciaxa estiver fechada
						casasFechadas+= 1
					elif mapa[x][y] == 'F':#caixa que estiver marcada
						casasFechadas-=1

	elif (linha == 8) and (0 < coluna < 8):
			for x in [linha-1, linha]:
				for y in [coluna-1, coluna, coluna+1]:
					if mapa[x][y] == ' ': #ciaxa estiver fechada
						casasFechadas+= 1
					elif mapa[x][y] == 'F':#caixa que estiver marcada
						casasFechadas-=1

	elif (coluna == 0) and (0 < linha < 8):
			for x in [coluna, coluna+1]:
				for y in [linha-1, linha, linha+1]:
					if mapa[y][x] == ' ': #ciaxa estiver fechada
						casasFechadas+= 1
					elif mapa[y][x] == 'F':#caixa que estiver marcada
						casasFechadas-=1

	elif (coluna == 8) and (0 < linha < 8):
			for x in [coluna-1, coluna]:
				for y in [linha-1, linha, linha+1]:
					if mapa[y][x] == ' ': #ciaxa estiver fechada
						casasFechadas+= 1
					elif mapa[y][x] == 'F':#caixa que estiver marcada
						casasFechadas-=1

	if casasFechadas!=0:
		prob = int(numero)/casasFechadas
		t.f = prob
		print(t)
		return prob
	else:
		return 0
	#retorn h(x) -> funcao heuristica

#definir a f(x)
'''
mapa=eval(sys.argv[1])
abertos=[]
fechados=[]
gerarListas(mapa, abertos, fechados)
print('Abertos:')
print(abertos)
print('\nFechados')
print(fechados)