import logging
import minesweeper as mns
import testeImagem as ti
import sys

class TipoNo:
    def __init__(self, x, y):
        self.__x=x
        self.__y=y
        self.__data=None

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
                if(self.__valido(a,b)):
                        no=TipoNo(a,b)
                        no.setData(mapa[a][b])
                        vizinhos.append(no)
        return vizinhos
    
    def __valido(self, x, y) :
        if (x < 0 or x > gridsize-1 or
            y < 0 or y > gridsize-1) :
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
        

class Game:
    def __init__(self):
        logging.basicConfig(filename='minesweeperIa.log', level=logging.DEBUG,
        format='%(levelname)s %(funcName)s => %(message)s')
        if(ia==1):
            self.__ia=AEstrela()
        elif(ia==2):
            self.__ia=BestFirst()

    def jogo(self):
        currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
        grid = []
        flags = []
        game=True
        cell=self.__ia.jogadaInicial()
        cellAbrir=(cell.getX(),cell.getY())
        if not grid:
            grid, mines = mns.setupgrid(gridsize, cellAbrir, numberofmines)

        while(game==True):
            cell=self.__ia.definirJogada(currgrid)
            if type(cell)==None:
                print('Perdeu, a lista de abertos ficou vazia')
                game==False
            else:
                cellAbrir=(cell.getX(),cell.getY())
                print(cellAbrir, cell.getData())
                if cell.getData()=='F':
                    game=mns.jogar(cellAbrir,currgrid,grid,flags,mines, flag=True)
                else:
                    game=mns.jogar(cellAbrir,currgrid,grid,flags,mines)
        return

class AEstrela:
    def __init__(self):
        self.__abertos=[]
        self.__fechados=[]
        self.__mapa=[]
        self.__conhecidos=[]
        self.__EstadoInicial=TipoNo(0,0)

    def __algoritmo(self):
        sucessores=[]
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
                    if c not in self.__abertos or c not in self.__fechados:
                        self.__abertos.append(c)
                self.__abertos.remove(m)
                self.__fechados.append(m)

    def __melhorNo(self):
        melhor=(0,0)
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

    def __jogadaValida(self,cell):
        if cell.getData()=='F':
            return False
        elif cell.getData()=='0':
            return False
        elif self.casasAAbrir(cell)==0:
            return False
        else:
            return True
        
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


class BestFirst:
    pass

    
'''
ia=eval(sys.argv[1])
gridsize=eval(sys.argv[2])
numberofmines=eval(sys.argv[3])
'''
print('Algoritmos:\nA*:1\nBestFirst:2')
ia= input('Selecione o Algoritmo(1 ou 2):')
gridsize=input('Selecione o tamanho do tabuleiro:')
numberofmines=input('Selecione o numero de bombas:')
ia=int(ia)
gridsize=int(gridsize)
numberofmines=int(numberofmines)
mine=Game()
mine.jogo()