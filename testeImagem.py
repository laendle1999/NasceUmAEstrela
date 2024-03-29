#testeImagem.py

from PIL import Image, ImageDraw, ImageFont
from TipoNo import TipoNo

comecoX = 12
comecoY = 15
tamX = 74
tamY = 73
sepX = 1
sepY = 2
contador = 0

celulasJaPostas = []
bas = Image.new("RGB",(2500,800),color=(255,255,255,0))

size = tamX, tamY

def posTabuleiro(x,y):
	return (comecoX + (x * (tamX + sepX))),(comecoY + (y * (tamY + sepY)))

def posArvore(x,y):
	return (10 + (150 * x)),(10 + (50 * y))

def objCasa(cell,x,y,ant,h):
	casa = {"cell": cell, "x": x, "y": y, "anterior": ant, "heuristica": h}
	return casa

def compararObj(cell,objCasa):
	if cell.getXY() == objCasa['cell'].getXY():
		return True
	else:
		return False

def buscarLista(cell,lista):
	celulasAnteriores=[]
	for c in celulasJaPostas:
		celulasAnteriores.append(c['cell'])
	if cell in celulasAnteriores:
		return True
	else:
		return False

'''

c1 = Image.open("casa1.png")
c1.thumbnail(size)
c2 = Image.open("casa2.png")
c2.thumbnail(size)
c3 = Image.open("casa3.png")
c3.thumbnail(size)
'''
def montarImagem(mapa,imagens):
	#FFFFFF
	#bomba.thumbnail(size)

	#i1.paste(c2,(12,15))
	#i1.show()
	i1 = Image.open("imagens/grade.png")

	x=0
	y=0

	for linha in mapa:
		for cell in linha:
			if cell == "F":
				cBan = Image.open("imagens/casaBan.png")
				cBan.thumbnail(size)
				i1.paste(cBan,posTabuleiro(y,x))
			elif cell == "X":
				bomba = Image.open("imagens/bomba.png")
				bomba.thumbnail(size)
				i1.paste(bomba,posTabuleiro(y,x))
			elif cell != " ":
				num = Image.open("imagens/casa" + cell + ".png")
				num.thumbnail(size)
				i1.paste(num,posTabuleiro(y,x))

			y+=1
		y=0
		x+=1

	imagens.append(i1)

def creategif(imagens,nome,duracao=100):
	imagens[0].save(str(nome)+'.gif', format='GIF', append_images=imagens[1:], save_all=True, duration=duracao, loop=0)



def fazerArvore(cells, cellAnt, arvore):
	x = 0
	w = 0
	celulasAnteriores=[]
	for c in celulasJaPostas:
		celulasAnteriores.append(c['cell'][:])

	global contador
	
	for c in celulasJaPostas:
		if c['cell'] == cellAnt.getXY():
			bas.paste(noVisitado(c['cell'],c['anterior'],c["heuristica"]),posArvore(c['x'],c['y']))

	arvore.append(bas.copy())


	for c in cells:
		if c.getXY() not in celulasAnteriores:
			if str(type(cellAnt)) == "<class 'NoneType'>":
				bas.paste(noArvore(c.getXY(),cellAnt,c.getF()),posArvore(x,contador))
				celulasJaPostas.append(objCasa(c.getXY(),x,contador,cellAnt,c.getF()))
			else:
				bas.paste(noArvore(c.getXY(),cellAnt.getXY(),c.getF()),posArvore(x,contador))
				celulasJaPostas.append(objCasa(c.getXY(),x,contador,cellAnt.getXY(),c.getF()))
			w = 1
			x+=1
	contador += w
	arvore.append(bas.copy())




def noArvore(cell,cellAnt,funcH):
	 
	img = Image.open("imagens/noArvore.png")
	sizeNo = 130, 390
	img.thumbnail(sizeNo)
	d = ImageDraw.Draw(img)
	
	d.text((5,15), str(cell), fill=(255, 255, 0))
	d.text((48,15), str(cellAnt), fill=(255, 255, 0))
	d.text((95,15), str(funcH), fill=(255, 255, 0))

	return img
	#img.show()

def noVisitado(cell,cellAnt,funcH):
	 
	img = Image.open("imagens/noArvoreVisitado.png")
	sizeNo = 130, 390
	img.thumbnail(sizeNo)
	d = ImageDraw.Draw(img)
	
	d.text((5,15), str(cell), fill=(255, 255, 0))
	d.text((48,15), str(cellAnt), fill=(255, 255, 0))
	d.text((95,15), str(funcH), fill=(255, 255, 0))

	return img
	#img.show()
 
#noArvore((3,5),(1,1),5)

