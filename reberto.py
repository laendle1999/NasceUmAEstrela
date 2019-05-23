#reberto.py agora vai jogar campo minado otarios
from dataclasses import dataclass
import sys
import time

@dataclass
class Tno_ad:
	cell: (int,int)
	f: float = -1
'''
def getNumero(mapa,x,y):
	return mapa[x][y]
'''

def getNumero(mapa,cell):
	x,y = cell
	return mapa[x][y]



#checa se a casa pertence ao tabuleiro
def valido(x, y) :
    if (x < 0 or x > 8 or
        y < 0 or y > 8) :
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

def checkNeighbors(mapa, cell):
	x,y = cell
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
			if cell != ' ':
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
			elif(int(cell)==0):
				print("oxi")
				fechados.append((x,y))
			elif(int(cell)!=0 and cell!=' ' and cell!='F'):
				print("gerarListas")
				print(str(x)+","+str(y))
				print(checkNeighbors(mapa,(x,y)))
				print(checarCasa(mapa,(x,y)))
				if(checkNeighbors(mapa,(x,y))==1 and checarCasa(mapa,(x,y)) == 0):
					abertos.append((x,y))
				else:
					fechados.append((x,y))
			y=y+1
		x=x+1

def checarCasa(mapa, cell):
	casasFechadas = 0
	bombas = 0
	x,y = cell
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			#print(str(a) + " " + str(b))
			if(valido(a,b)):
				if(mapa[a][b] == ' '):
					casasFechadas+= 1
				elif(mapa[a][b] == 'F'):
					bombas += 1

	return (int(mapa[x][y]) - bombas)/ casasFechadas


def casasAAbrir(mapa, cell):
	linha, coluna = cell
	casasFechadas = 0
	for a in range(linha-1, linha+1):
		for b in range(coluna-1, coluna+1):
			if(valido(a,b)):
				if(mapa[a][b] == ' '):
					casasFechadas+= 1

	return casasFechadas


def funcHeurisitca(mapa,cell):
	return casasAAbrir(mapa,cell) + contarCasas(mapa)


def encontrarBombas(mapa):
	from minesweeper import getneighbors
	vizinhos = []
	probRedor = []
	bombas = []
	x = 0
	for linha in mapa:
		y = 0
		for cell in linha:
			if cell == " ":
				vizinhos = getneighbors(mapa,x,y)
				print(vizinhos)
				for v in vizinhos:
					if(getNumero(mapa,v) != " "):
						#print(v)
						#print(checarCasa(mapa,v))
						probRedor.append(checarCasa(mapa,v))
				if probRedor:
					if max(probRedor) == 1:
						bombas.append((x,y))
					probRedor = []	
			y+=1
		x+=1

	return bombas


def aEstrelaBusca():
	from minesweeper import setupgrid
	from minesweeper import jogar

	abertos=[]
	fechados=[]
	
	gridsize = 9
	numberofmines = 10

	grid = []
	flags = []
	starttime = 0
	
	currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
	cell = (0,0)

	if not grid:
		grid, mines = setupgrid(gridsize, cell, numberofmines)
	#if not starttime:
		#starttime = time.time()

	jogar(cell,currgrid,grid,flags,mines)
	while True:
		bombas = []
		bombas = encontrarBombas(currgrid)
		print(bombas)
		if bombas:
			for b in bombas:
				jogar(b,currgrid,grid,flags,mines,flag=True)

		gerarListas(currgrid, abertos, fechados)
		temp = 0
		val = 0
		cellAbrir = (0,0)
		if contarCasas(currgrid) == 81:
			print("Acabou o Jogo")
			break

		print("abertos: ")
		print(abertos)
		if abertos:
			for cell in abertos:
				temp = funcHeurisitca(currgrid,cell)
				if(temp > val):
					cellAbrir = cell
					val = temp

		jogar(cellAbrir,currgrid,grid,flags,mines)
		input("Pressione <enter> para continuar")










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

mapa=eval(sys.argv[1])
abertos=[]
fechados=[]
gerarListas(mapa, abertos, fechados)
print('Abertos:')
print(abertos)
print('\nFechados')
print(fechados)
'''

aEstrelaBusca()