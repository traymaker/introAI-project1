import numpy as np 
import pygame as pg

from binaryHeap import *
from random import *
from util import * 

class AStar:
	def __init__(self, screen, grid, start_state, goal_state):
		self.screen = screen
		self.grid = grid
		self.start_state = start_state 
		self.goal_state = goal_state

	def getH(self, a, b):
		#returns the scalar distance from point A, to point B
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	def show_Astar(self, tieBreak):
		#initial states
		neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		close_set = set()

		reverse_path = {}
		total_path = []

		gscore = {self.start_state: 0}
		fscore = {self.start_state: self.getH(self.start_state, self.goal_state)}

		open_heap = binaryHeap()
		open_heap.add((fscore[self.start_state], self.start_state))

		#The algorithm
		while open_heap:
			
			#if there is nothing left in the open heap
			try:
				current = open_heap.remove()[1]
			except:
				print('Path Not Found')
				return total_path

			#Plot and return total_path once found
			if current == self.goal_state:
				total_path = []

				while current in reverse_path:
					pg.draw.rect(self.screen, YELLOW,
									 [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
									  SIZE, SIZE])
					total_path.append(current)
					current = reverse_path[current]
				pg.display.update()
				return total_path

			close_set.add(current)

			#Expand Neighbors and find the next best move
			for i, j in neighbors:
				neighbor = current[0] + i, current[1] + j

				tempG = gscore[current] + self.getH(current, neighbor)

				if 0 <= neighbor[0] < WIDTH:
					if 0 <= neighbor[1] < HEIGHT:
						if self.grid[neighbor[0]][neighbor[1]] == 1:
							continue
					else:
						continue
				else:
					continue

				if neighbor in close_set and tempG >= gscore.get(neighbor, 0):
					continue
				if (tieBreak == 0): #low g-value tie-break
					if tempG < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap.get_heap()]:
						reverse_path[neighbor] = current
						gscore[neighbor] = tempG
						fscore[neighbor] = tempG + self.getH(neighbor, self.goal_state)
						open_heap.add((fscore[neighbor], neighbor))

						#Plot visited neighbors
						# pg.draw.rect(self.screen, BLUE,
						# 			 [(PAD + SIZE) * neighbor[1] + PAD, (PAD + SIZE) * neighbor[0] + PAD,
						# 			  SIZE, SIZE])
						# pg.display.update()
				elif(tieBreak == 1): #high g-value tie-break
					if tempG > gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap.get_heap()]:
						reverse_path[neighbor] = current
						gscore[neighbor] = tempG
						fscore[neighbor] = tempG + self.getH(neighbor, self.goal_state)
						open_heap.add((fscore[neighbor], neighbor))
						
						#Plot visited neighbors
						# pg.draw.rect(self.screen, BLUE,
						# 			 [(PAD + SIZE) * neighbor[1] + PAD, (PAD + SIZE) * neighbor[0] + PAD,
						# 			  SIZE, SIZE])
						# pg.display.update()
			
		return total_path

	def show_AdaptiveAstar(self):
		new_fscore = self.rfas()
		
		neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		close_set = set()

		reverse_path = {}

		gscore = {self.start_state: 0}
		
		open_heap = binaryHeap()

		open_heap.add(open_heap, (new_fscore[self.start_state], self.start_state))

		while open_heap:
			current = open_heap.remove()[1]

			if current == self.goal_state:
				total_path = []

				while current in reverse_path:
					pg.draw.rect(self.screen, BLUE,
									 [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
									  SIZE, SIZE])
					pg.display.update()
					total_path.append(current)
					current = reverse_path[current]
				return total_path

			close_set.add(current)

			for i, j in neighbors:
				neighbor = current[0] + i, current[1] + j

				tempG = gscore[current] + self.getH(current, neighbor)

				if 0 <= neighbor[0] < WIDTH:
					if 0 <= neighbor[1] < HEIGHT:
						if self.grid[neighbor[0]][neighbor[1]] == 1:
							continue
					else:
						continue
				else:
					continue

				if neighbor in close_set and tempG >= gscore.get(neighbor, 0):
					continue

				if tempG > gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap.get_heap()]:
					reverse_path[neighbor] = current
					gscore[neighbor] = tempG
					new_fscore[neighbor] = tempG + self.getH(neighbor, self.goal_state)
					open_heap.add(open_heap, (new_fscore[neighbor], neighbor))
					
					# pg.draw.rect(self.screen, BLUE,
					# 				 [(PAD + SIZE) * neighbor[1] + PAD, (PAD + SIZE) * neighbor[0] + PAD,
					# 				  SIZE, SIZE])
					# pg.display.update()

		print('Path Not Found')
		return total_path
	
	#hidden repeat forward Astar for AdaptiveAstar
	def rfas(self): 
		neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

		close_set = set()

		reverse_path = {}

		gscore = {self.start_state: 0}
		fscore = {self.start_state: self.getH(self.start_state, self.goal_state)}

		open_heap = binaryHeap()
		open_heap.add(open_heap, (fscore[self.start_state], self.start_state))

		while open_heap:
			current = open_heap.remove()[1]

			if current == self.goal_state:
				return fscore

			close_set.add(current)

			for i, j in neighbors:
				neighbor = current[0] + i, current[1] + j

				tempG = gscore[current] + self.getH(current, neighbor)

				if 0 <= neighbor[0] < WIDTH:
					if 0 <= neighbor[1] < HEIGHT:
						if self.grid[neighbor[0]][neighbor[1]] == 1:
							continue
					else:
						continue
				else:
					continue

				if neighbor in close_set and tempG >= gscore.get(neighbor, 0):
					continue

				if tempG > gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap.get_heap()]:
					# print(neighbor)

					reverse_path[neighbor] = current
					gscore[neighbor] = tempG
					fscore[neighbor] = tempG + self.getH(neighbor, self.goal_state)
					open_heap.add(open_heap, (fscore[neighbor], neighbor))
					
					# pg.draw.rect(self.screen, BLUE,
					# 				 [(PAD + SIZE) * neighbor[1] + PAD, (PAD + SIZE) * neighbor[0] + PAD,
					# 				  SIZE, SIZE])
					# pg.display.update()

		print('Path Not Found')
		return fscore