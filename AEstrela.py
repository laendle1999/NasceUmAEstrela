from TipoNo import TipoNo
from Agente import Agente
import logging

class AEstrela(Agente):
	def __init__(self):
	 Agente.__init__(self)
	 self.__abertos=[]
	 self.__fechados=[]

	def __algoritmo(self):
	 sucessores=[]
	 self.__abertos=[]
	 self.__fechados=[]
	 if not self.__abertos and not self.__fechados:
		 p=super(self).__EstadoInicial
		 self.__funcHeurisitca(p)
		 self.__abertos.append(p)
	 while(True):
		 m=self.__melhorNo()
		 if super(self).__jogadaValida(m):
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

  
	def __funcHeurisitca(self,cell):
		cell.setF(self.__g(cell) + self.__h(cell))

  

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
	
