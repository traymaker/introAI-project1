import pygame as pg
import time, timeit
import numpy as np 

from util import *
from AStar import *

class Cell(object):	
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		#to be used in A*
		self.parent = None
		self.f = 0
		self.g = 0
		self.h = 0

def initMap():
	n = input('Enter a map number from 0 to 49: \n')

	while((int(n) > 49) or (int(n) < 0)):
		n = input('Invalid Choice! Enter a map number 0 to 49: \n')
	
	fp = 'Maps/' + 'map' + str(n) + '.txt'
	fs = open(fp, 'r')
	lines = fs.readlines()
	tempArray = []
	tempCell = None

	for line in lines:
		line = line.strip().split(',')
		line = list(map(int, line))
		tempArray.append(line)

	for i in range(DIM):
		for j in range(DIM):
			tempArray[i][j] = Cell(i, j, tempArray[i][j])

	return tempArray

pg.init()
screen = pg.display.set_mode((((DIM * 8) + 1), ((DIM * 8) + 1)))
pg.display.set_caption("DisplayStar")
clock = pg.time.Clock()
pg.display.flip()

distance = 0
start = 0.0
stop = 0.0
runTime = 0.0
gValue = 0 #gValue Hi/Lo 0 is low 1 is high
done = False
start_state = (0, 0)
goal_state  = (100, 100)

regAstar = AStar(DIM, screen, start_state, goal_state) 

#TODO
#implement algo controllers in AStar.py
while not done:
	for event in pg.event.get():  
		if (event.type == pg.QUIT): #Exit button quits program  
			done = True  
		elif event.type == pg.KEYDOWN:
			if (event.key == pg.K_c):	#c key press Clears screen of previous A* Star Path on current map
				#TODO
				#make this a function too
				for row in range(DIM):
					for column in range(DIM):
						if (grid[row][column].color == 0):
							color = WHITE
							grid[row][column].color = 0
							pg.draw.rect(screen, color, [(PAD + SIZE) * column + PAD, (PAD + SIZE) * row + PAD,SIZE, SIZE])

				pg.display.flip()
				time = 0
				distance = 0
				print('Path Cleared')
			elif (event.key == pg.K_l):	#l key press Loads/initializes a new map
				grid = initMap()
				#TODO
				#put this for in the initMap function 
				for row in range(DIM):
					for column in range(DIM):
						color = BLUE
						
						if grid[row][column].color == 0:
							color = WHITE
						elif grid[row][column].color == 1:
							color = BLACK
						elif grid[row][column].color == 2:
							color = RED
						elif grid[row][column].color == 3:
							color = GREEN
						pg.draw.rect(screen, color,
							[(PAD + SIZE) * column + PAD, (PAD + SIZE) * row + PAD, SIZE, SIZE])

				pg.display.flip()
			elif (event.key == pg.K_1):	#Forward A* with Low G-Value Tie-Break:
				print("test")
			# elif event.key == pg.K_2:	#Forward A* with High G-Value Tie-Break:
			# elif event.key == pg.K_3:	#Backward A* with Low G-Value Tie-Break:
			# elif event.key == pg.K_4:	#Backward A* with High G-Value Tie-Break:
			# elif event.key == pg.K_5:	#Adaptive A* with Low G-Value Tie-Break:
			# elif event.key == pg.K_6:	#Adaptive A* with High G-Value Tie-Break:

	pg.display.flip()

pg.quit()