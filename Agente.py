#Agente.py
from TipoNo import TipoNo
import logging
import abc

class Agente:
	"""docstring for Agente"""
	def __init__(self):
		self.__mapa=[]
		self.__conhecidos=[]
		self.__EstadoInicial=TipoNo(0,0)

	def __melhorNo(self):
	 return

	def _algoritmo(self):
		return

	def __funcHeurisitca(self,cell):
		return

	def __g(self, cell):
	 return self.__contarCasas()

	def __h(self, cell):
	 return self.casasAAbrir(cell) + 100 * (1 - cell.checarCasa(self.__mapa))

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
	 return

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

