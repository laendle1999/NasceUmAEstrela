import logging
from AEstrela import AEstrela 
#from BestFrist import BestFrist
import minesweeper as mns
import testeImagem as ti
import sys

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

        while(game):
            cell=self.__ia.definirJogada(currgrid)
            if str(type(cell)) == "<class 'NoneType'>": #funciona, nao me julgue
                print('Perdeu, a lista de abertos ficou vazia')
                game=False
            else:
                cellAbrir=(cell.getX(),cell.getY())
                print(cellAbrir, cell.getData())
                if cell.getData()=='F':
                    game=mns.jogar(cellAbrir,currgrid,grid,flags,mines, flag=True)
                else:
                    game=mns.jogar(cellAbrir,currgrid,grid,flags,mines)
        return


    
if sys.argv:
    ia=sys.argv[1]
    gridsize=sys.argv[2]
    numberofmines=sys.argv[3]
else:
    print('Algoritmos:\nA*:1\nBestFirst:2')
    ia= input('Selecione o Algoritmo(1 ou 2):')
    gridsize=input('Selecione o tamanho do tabuleiro:')
    numberofmines=input('Selecione o numero de bombas:')
ia=int(ia)
gridsize=int(gridsize)
numberofmines=int(numberofmines)
mine=Game()
mine.jogo()