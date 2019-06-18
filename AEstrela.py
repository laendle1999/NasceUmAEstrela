from TipoNo import TipoNo
from testeImagem import fazerArvore
import logging

class AEstrela:
	def __init__(self):
		self.__imagem=[]
		self.__abertos=[]
		self.__fechados=[]
		self.__mapa=[]
		self.__conhecidos=[]
		self.__EstadoInicial=TipoNo(0,0)

	def __algoritmo(self):
		sucessores=[]
		self.__abertos=[]
		self.__fechados=[]
		
		if not self.__abertos and not self.__fechados:
			p=self.__EstadoInicial
			self.__funcHeurisitca(p)
			self.__abertos.append(p)
		while(True):
			m=self.__melhorNo()
			if self.__jogadaValida(m):
				return m
			elif not self.__abertos:
				return None
			else:
				sucessores=m.getVizinhos(self.__mapa)
				for c in sucessores:
					self.__funcHeurisitca(c)
					if c not in self.__abertos and c not in self.__fechados:
						self.__abertos.append(c)
				self.__abertos.remove(m)
				self.__fechados.append(m)

	def __melhorNo(self):
		melhor=TipoNo(0,0)
		val=0
		temp=0
		for n in self.__abertos:
			temp=n.getF()
			if temp>val:
				melhor=n
				val=temp
		return melhor

	def __funcHeurisitca(self,cell):
		cell.setF(self.__g(cell) + self.__h(cell))

	def __g(self, cell):
		return self.__contarCasas()

	def __h(self, cell):
		return self.casasAAbrir(cell) + 100 * (1 - cell.checarCasa(self.__mapa))
	
	def getArvore(self):
			return self.__imagem

	def getAbertos(self):
			return self.__abertos


	def __jogadaValida(self,cell):
		if cell.getData()=='F':
			return False
		elif cell.getData()=='0':
			return False
		elif self.casasAAbrir(cell)==0:
			return False
		elif cell.getData()==' ':
			return False
		elif cell.checarCasa(self.__mapa)==0:
			return True
		else:
			return False
		
	def __contarCasas(self):
		x = 0
		for linha in self.__mapa:
			for cell in linha:
				if cell != " ":
					x+=1
		return x

	def casasAAbrir(self, cell):
		aabrir=[]
		aabrir=cell.vizinhosAAbrir(self.__mapa)
		casasFechadas=len(aabrir)
		return casasFechadas


	def definirJogada(self, mapa):
		bombas=[]
		self.__mapa=mapa
		bombas=self.encontrarBombas()
		if bombas:
			x,y=bombas[-1]
			jogada=TipoNo(x,y)
			jogada.setData('F')
		else:
			jogada=self.__algoritmo()

		return jogada

	def encontrarBombas(self):
		vizinhos = []
		probRedor = []
		bombas = []
		x = 0
		for linha in self.__mapa:
			y = 0
			for cell in linha:
				if cell == " ":
					no=TipoNo(x,y)
					vizinhos = no.getVizinhos(self.__mapa)
					logging.info(str(vizinhos))
					for v in vizinhos:
						if(v.getData() != " " and v.getData() != "F"):
							probRedor.append(v.checarCasa(self.__mapa))
					if probRedor:
						if max(probRedor) == 1:
							bombas.append((x,y))
						probRedor = []	
				y+=1
			x+=1

		return bombas
	
	def jogadaInicial(self):
		return self.__EstadoInicial



