"""A command line version of Minesweeper"""
import random
import re
import time
import sys
import subprocess
#import reberto as rere
from string import ascii_lowercase
from testeImagem import montarImagem, creategif

imagens=[]

def montarGif():
	creategif(imagens,"game")


def setupgrid(gridsize, start, numberofmines):
	emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]

	mines = getmines(emptygrid, start, numberofmines)

	for i, j in mines:
		emptygrid[i][j] = 'X'

	grid = getnumbers(emptygrid)

	return (grid, mines)


def showgrid(grid):
	gridsize = len(grid)

	horizontal = '   ' + (4 * gridsize * '-') + '-'

	# Print top column letters
	toplabel = '     '

	for i in ascii_lowercase[:gridsize]:
		toplabel = toplabel + i + '   '

	print(toplabel + '\n' + horizontal)

	# Print left row numbers
	for idx, i in enumerate(grid):
		row = '{0:2} |'.format(idx + 1)

		for j in i:
			row = row + ' ' + j + ' |'

		print(row + '\n' + horizontal)

	print('')


def getrandomcell(grid):
	gridsize = len(grid)

	a = random.randint(0, gridsize - 1)
	b = random.randint(0, gridsize - 1)

	return (a, b)


def getneighbors(grid, rowno, colno):
	gridsize = len(grid)
	neighbors = []

	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
				neighbors.append((rowno + i, colno + j))

	return neighbors


def getmines(grid, start, numberofmines):
	mines = []
	neighbors = getneighbors(grid, *start)

	for i in range(numberofmines):
		cell = getrandomcell(grid)
		while cell == start or cell in mines or cell in neighbors:
			cell = getrandomcell(grid)
		mines.append(cell)

	return mines


def getnumbers(grid):
	for rowno, row in enumerate(grid):
		for colno, cell in enumerate(row):
			if cell != 'X':
				# Gets the values of the neighbors
				values = [grid[r][c] for r, c in getneighbors(grid,
															  rowno, colno)]

				# Counts how many are mines
				grid[rowno][colno] = str(values.count('X'))

	return grid


def showcells(grid, currgrid, rowno, colno):
	# Exit function if the cell was already shown
	if currgrid[rowno][colno] != ' ':
		return

	# Show current cell
	currgrid[rowno][colno] = grid[rowno][colno]

	# Get the neighbors if the cell is empty
	if grid[rowno][colno] == '0':
		for r, c in getneighbors(grid, rowno, colno):
			# Repeat function for each neighbor that doesn't have a flag
			if currgrid[r][c] != 'F':
				showcells(grid, currgrid, r, c)


def abrirVizinhos(grid, currgrid, rowno, colno):
	for r, c in getneighbors(grid, rowno, colno):
			# Repeat function for each neighbor that doesn't have a flag
			if currgrid[r][c] != 'F':
				showcells(grid, currgrid, r, c)
				if grid[r][c] == 'X':
					print('Game Over\n')
					showgrid(grid)
					#if playagain():
					#	playgame()
					return 


def playagain():
	choice = input('Play again? (y/n): ')

	return choice.lower() == 'y'


def parseinput(inputstring, gridsize, helpmessage):
	cell = ()
	flag = False
	message = "Invalid cell. " + helpmessage

	pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[gridsize - 1])
	validinput = re.match(pattern, inputstring)

	if inputstring == 'help':
		message = helpmessage
	elif validinput==None:
		return 1
	elif validinput:
		rowno = int(validinput.group(2)) - 1
		colno = ascii_lowercase.index(validinput.group(1))
		flag = bool(validinput.group(3))

		if -1 < rowno < gridsize:
			cell = (rowno, colno)
			message = ''

	return {'cell': cell, 'flag': flag, 'message': message}


def jogar(cell,currgrid,grid,flags,mines,flag=False):
	if cell:
		print('\n\n')
		rowno, colno = cell
		currcell = currgrid[rowno][colno]
		
		if flag:
			# Add a flag if the cell is empty
			if currcell == ' ':
				currgrid[rowno][colno] = 'F'
				flags.append(cell)
			# Remove the flag if there is one
			elif currcell == 'F':
				currgrid[rowno][colno] = ' '
				flags.remove(cell)

		elif grid[rowno][colno] == 'X':
			print('Game Over\n')
			showgrid(grid)
			return False

		elif currcell == ' ':
			showcells(grid, currgrid, rowno, colno)

		else:
			abrirVizinhos(grid, currgrid, rowno, colno)
		
		for linha in currgrid:
			for cell in linha:
				if cell == 'X':
					return False

		if set(flags) == set(mines):
			print('Voce Ganhou.\n')
			#montarImagem(grid,imagens)
			#montarGif()
			showgrid(grid)
			return False

		#montarImagem(currgrid,imagens)
		showgrid(currgrid)
		return True