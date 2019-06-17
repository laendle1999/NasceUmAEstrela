from TipoNo import TipoNo
from Agente import Agente
import logging

class BestFirst(Agente):
	
	def __init__(self):
		Agente.__init__(self)
		self._vizinhos=[]
		self.__visitados=[]


	def algoritmo(self):
		sucessores=[]
		self._vizinhos=[]
	 self.__visitados=[]
	 if not self._vizinhos and not self.__visitados:
		 p=self.__EstadoInicial
		 self.__funcHeurisitca(p)
		 self._vizinhos.append(p)
	 while(True):
		 m=self.__melhorNo()
		 if self.__jogadaValida(m):
		  return m
		 elif not self._vizinhos:
		  return None
		 else:
		  sucessores=m.getVizinhos(self.__mapa)
		  for c in sucessores:
			  self.__funcHeurisitca(c)
			  if c not in self.__visitados:
			   self._vizinhos.append(c)
		  self._vizinhos.remove(m)
		  self.__visitados.append(m)



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


	def __funcHeurisitca(self,cell):
		cell.setF(self.__h(cell))

	def __melhorNo(self):
	 melhor=TipoNo(0,0)
	 val=0
	 temp=0
	 for n in self._vizinhos:
		 temp=n.getF()
		 if temp>val:
		  melhor=n
		  val=temp
	 return melhor
