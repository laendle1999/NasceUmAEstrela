class TipoNo:
	def __init__(self, x, y, gridsize = 8):
		self.__x=x
		self.__y=y
		self.__data=None
		self._gridsize=gridsize

	def __eq__(self, outro):
		return self.__x == outro.getX() and self.__y == outro.getY()
	
	def setF(self, f):
		self.__f=f

	def getF(self):
		return self.__f
	
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def setData(self, data):
		self.__data=data

	def getData(self):
		return self.__data

	def getVizinhos(self, mapa):
		vizinhos=[]
		for a in range(self.__x-1, self.__x+2):
			for b in range(self.__y-1, self.__y+2):
				if(a==self.__x and b==self.__y):
					continue
				if(self.__valido(a,b)):
						no=TipoNo(a,b)
						no.setData(mapa[a][b])
						vizinhos.append(no)
		return vizinhos
	
	def __valido(self, x, y) :
		if (x < 0 or x > self._gridsize-1 or
			y < 0 or y > self._gridsize-1) :
			return False
		return True

	def vizinhosAAbrir(self, mapa):
		vizinhos=[]
		fechadas=[]
		vizinhos=self.getVizinhos(mapa)
		for cell in vizinhos:
			if cell.getData()==' ':
				fechadas.append(cell)
		return fechadas

	def checarCasa(self, mapa):
		if self.__data=='F' or self.__data==' ':
			return 0
		bombas = 0
		vizinhos=[]
		fechadas=[]
		vizinhos=self.getVizinhos(mapa)
		fechadas=self.vizinhosAAbrir(mapa)
		casasFechadas=len(fechadas)
		for casa in vizinhos:
			if casa not in fechadas:
				if casa.getData()=='F':
					bombas+=1
		if casasFechadas != 0 and mapa[self.__x][self.__y]!=' ':
			return (int(mapa[self.__x][self.__y]) - bombas)/ casasFechadas
		else:
			return 0
		
