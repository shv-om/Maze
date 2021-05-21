"""
Wilson's Algorithm

1.  Choose a random cell and add it to the visited list
2.  Choose another random cell (Don’t add to visited list). This is the current cell
3.  Choose a random cell that is adjacent to the current cell (Don’t add to visited list). This is your new current cell.
4.  Save the direction that you traveled on the previous cell
5.  If the current cell is not in the visited cells list
        Go to 3

6.  Else
        Starting at the cell selected in step 2, follow the arrows and remove the edges that are crossed.
        Add all cells that are passed into the visited list

7.  If all cells have not been visited
        Go to 2

"""

import numpy as np
import random

class Maze:

	def __init__(self, size):
		self.size = size
		self.current_cell = (0, 0)
		self.visited = []
		self.path = []
		self.temp_path = []
		self.direction = []
		self.opposite = {'l': 'r', 'r': 'l', 't': 'b', 'b': 't'}
		
		self.maze_array = np.zeros((self.size, self.size), dtype=np.int8)
		
		self.create_maze()
	
			
	def choose_random(self):
		point = (random.choice(range(1, self.size-1)), random.choice(range(1, self.size-1)))
		
		if point not in self.visited:
			return point
		else:
			return self.choose_random()
	
	
	def mark_visited(self, cell, i):
		self.maze_array[cell[0]][cell[1]] = i
		self.visited.append(cell)
	
	
	def move_direction(self, cell):
		temp = ['l', 'r', 't', 'b']
		
		if self.direction != []:
			prev = self.opposite[self.direction[-1]]
			temp.remove(prev)
			#print(temp, prev)
		
		di = random.choice(temp)
		
		self.direction.append(di)
		
		if cell != None:
			if cell[1] > 0:
				if di == 'l':
					cell = (cell[0], cell[1]-1)
			if cell[1] < self.size-1:
				if di == 'r':
					cell = (cell[0], cell[1]+1)
			if cell[0] > 0:
				if di == 't':
					cell = (cell[0]-1, cell[1])
			if cell[0] < self.size-1:
				if di == 'b':
					cell = (cell[0]+1, cell[1])
		
		return cell
		
	
	def create_path(self):
		
		self.current_cell = self.choose_random()
		#print("current cell", self.current_cell)
		
		while True:
			if self.current_cell not in self.visited:
				if self.current_cell not in self.temp_path:
					self.temp_path.append(self.current_cell)
					self.current_cell = self.move_direction(self.current_cell)
				else:
					self.temp_path = []
					self.path.extend(self.direction)
					self.direction = []
					self.create_path()
			else:
				#self.current_cell = self.choose_random()
				break
	
	
	def create_maze(self):
		
		start_point = self.choose_random()
		print(start_point)
		self.mark_visited(start_point, 1)
		
		while True:
			if len(self.visited) <= (self.size)**2:
				self.create_path()
				for i in self.temp_path:
					self.mark_visited(i, 1)
			else:
				print(len(self.visited))
				break
		
		return self.maze_array
		



maze = Maze(30)
print(maze.maze_array)
#print(maze.visited[-1])
#print(maze.path, len(maze.path))

