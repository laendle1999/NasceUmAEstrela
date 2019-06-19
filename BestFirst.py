from TipoNo import TipoNo
import logging

class BestFirst:
    def __init__(self):
        self.__visitados=[]
        self.__mapa=[]
        self.__contador=0
        self.__casasAnalisadas=[]
        self.__EstadoInicial=TipoNo(0,0)

    def __algoritmo(self, cell):
        self.__visitados.append(cell)
        if self.__jogadaValida(cell):
            return cell
        vizinhos=[]
        validas=[]
        vizinhos=cell.getVizinhos(self.__mapa)
        for v in vizinhos:
            if v not in self.__visitados:
                self.__funcHeurisitca(v)
                validas.append(v)
        if len(validas)==0:
            return None
        else:
            while(validas):
                m=self.__melhorNo(validas)
                resultado=self.__algoritmo(m)
                if str(type(resultado))!="<class 'NoneType'>":
                    return resultado
                else:
                    validas.remove(m)


    def __melhorNo(self, vizinhos):
        melhor=TipoNo(0,0)
        val=0
        temp=0
        for n in vizinhos:
            temp=n.getF()
            if temp>val:
                melhor=n
                val=temp
        return melhor

    def __funcHeurisitca(self,cell):
        cell.setF(self.__h(cell))

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
        self.__visitados=[]
        bombas=[]
        self.__mapa=mapa
        bombas=self.encontrarBombas()
        if bombas:
            x,y=bombas[-1]
            jogada=TipoNo(x,y)
            jogada.setData('F')
        else:
            jogada=self.__algoritmo(self.__EstadoInicial)
        self.__contador+=1
        return jogada

    def encontrarBombas(self):
        vizinhos = []
        probRedor = []
        bombas = []
        x = 0
        for linha in self.__mapa:
            y = 0
            for cell in linha:
                if cell == ' ':
                    no=TipoNo(x,y)
                    vizinhos = no.getVizinhos(self.__mapa)
                    logging.info(str(vizinhos))
                    for v in vizinhos:
                        if(v.getData() != ' ' and v.getData() != 'F'):
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


