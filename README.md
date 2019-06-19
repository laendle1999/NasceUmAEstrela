# NasceUmAEstrela

 Algoritmo em python para resolver o problema do jogo Campo Minado com algoritmos de busca A* e Best-First

### Requisitos:
- Pillow

### Arquivos:
>reberto.py: Classe main que recebe dos algoritmos a jogada e passa ao jogo

>TipoNo.py: Classe basica com funções para os nós das listas

>minnesweeper.py: Jogo do campo minado

>TesteImagem.py: Arquivo com funções para fazer a arvore animada e o jogo

>AEstrela.py e BestFirst.py: Classes com os algoritmos de busca heuristica

### Como Execultar:
Para execultar o código é necessario passar por linha de comando as escolhas de algortmo de busca(1 para A* e 2 para Best-First), tamanho do tabuleiro e numero de bombas
```
python3 reberto.py [algoritmo de escolha] [tamanho do tabuleiro] [ numero de bombas]
```
### Resultados
Foram testados 100 vezes os algoritmos, fazendo uma média e como resultado obtivemos que
- Best-First: 52%
- A*:  52%

PS. Sorry, all code in portuguese
