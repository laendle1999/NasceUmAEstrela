#reberto.py agora vai jogar campo minado otarios
from dataclasses import dataclass
import time
import logging
logging.basicConfig(filename='minesweeperIa.log', level=logging.DEBUG,
        format='%(levelname)s %(funcName)s => %(message)s')


@dataclass
class Tno_ad:
	cell: (int,int)
	f: float = -1

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
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			if(valido(a,b)):
				if(mapa[a][b]== ' '):
					return 1
	return 0

def checkNeighbors(mapa, cell):
	x,y = cell
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
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

def recalcularListas(mapa, abertos, fechados):
	x=0
	for linha in mapa:
		y=0
		for cell in linha:
			if((x,y) in abertos):
				if(int(cell)!=0 and cell!=' ' and cell!='F'):
					logging.info("Casa (%d,%d): Vizinhos %d, Bomba %f",x,y,checkNeighbors(mapa,(x,y)),checarCasa(mapa,(x,y)))
					if(checkNeighbors(mapa,(x,y))==0):
						abertos.remove((x,y))
						fechados.append((x,y))
			else:
				if((x,y) not in fechados):
					if(cell=='F'):
						fechados.append((x,y))
					elif(cell==" "):
						x=x
					elif(int(cell)==0):
						logging.debug("Casa (%d,%d): valor 0",x,y)
						fechados.append((x,y))
					elif(int(cell)!=0 and cell!=' ' and cell!='F'):
						logging.info("Casa (%d,%d): Vizinhos %d, Bomba %f",x,y,checkNeighbors(mapa,(x,y)),checarCasa(mapa,(x,y)))
						if(checkNeighbors(mapa,(x,y))==1):
							abertos.append((x,y))
						else:
							fechados.append((x,y))
			y=y+1
		x=x+1


#gera a lista de nós abertos e fechados
def gerarListas(mapa, abertos, fechados):
	if not abertos:
		x=0
		for linha in mapa:
			y=0
			for cell in linha:
				if(cell=='F'):
					fechados.append((x,y))
				elif(cell==" "):
					x=x
				elif(int(cell)==0):
					logging.debug("Casa (%d,%d): valor 0",x,y)
					fechados.append((x,y))
				elif(int(cell)!=0 and cell!=' ' and cell!='F'):
					logging.info("Casa (%d,%d): Vizinhos %d, Bomba %f",x,y,checkNeighbors(mapa,(x,y)),checarCasa(mapa,(x,y)))
					if(checkNeighbors(mapa,(x,y))==1):
						abertos.append((x,y))
					else:
						fechados.append((x,y))
				y=y+1
			x=x+1
	else:
		recalcularListas(mapa, abertos, fechados)

def checarCasa(mapa, cell):
	casasFechadas = 0
	bombas = 0
	x,y = cell
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			if(valido(a,b)):
			#print(str(a) + " " + str(b))
				if(mapa[a][b] == ' '):
					casasFechadas+= 1
				elif(mapa[a][b] == 'F'):
					bombas += 1

	if casasFechadas != 0:
		return (int(mapa[x][y]) - bombas)/ casasFechadas
	else:
		return 0


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
	return casasAAbrir(mapa,cell) + contarCasas(mapa) + 100 * (1 - checarCasa(mapa,cell))


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
				logging.info(str(vizinhos))
				for v in vizinhos:
					if(getNumero(mapa,v) != " " and getNumero(mapa,v) != "F"):
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
		logging.info("Rodando")
		bombas = []
		bombas = encontrarBombas(currgrid)
		#print(bombas)
		if bombas:
			for b in bombas:
				jogar(b,currgrid,grid,flags,mines,flag=True)

		gerarListas(currgrid, abertos, fechados)
		temp = 0
		val = 0
		cellAbrir = (0,0)
		if set(flags) == set(mines):
			print("Acabou o Jogo")
			break

		logging.info("Abertos: " + str(abertos))
		if abertos:
			for cell in abertos:
				temp = funcHeurisitca(currgrid,cell)
				if(temp > val):
					cellAbrir = cell
					val = temp

		

		jogar(cellAbrir,currgrid,grid,flags,mines)
		logging.info(str(currgrid))
		#input("Pressione <enter> para continuar")
		game = True
		for linha in currgrid:
			for cell in linha:
				if cell == 'X':
					print("Acabou o Jogo")
					game = False
		
		if not game:
			break


aEstrelaBusca()