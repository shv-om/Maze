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

import turtle
import random
import numpy as np

class Maze:

	def __init__(self, size):
		self.width = size
		self.height = size
		self.current_cell = (0, 0)
		self.visited = []					# to mark Visited Nodes
		self.path_directions = []			# chosen direction list
		self.path = []						# collection of all chosen nodes (moves) per iteration
		self.direction = ['l', 'r', 't', 'b']
		self.opposites = {'l': 'r', 'r': 'l', 't': 'b', 'b': 't'}

		# list containing all the cells to help in choosing random cells
		self.cells = [(i, j) for i in range(size) for j in range(size)]

		self.maze_array = np.zeros((self.width, self.height), dtype=np.int8)


	def update_cell(self, cell, n=1):
		# to update the cell value
		x, y = cell
		self.maze_array[x][y] = n

	
	def choose_cell(self):
		chosen = random.choice(self.cells)
		return chosen


	def mark_visited(self, temp_cells):
		for cell in temp_cells:
			# update the visited list
			self.visited.append(cell)
			#print(cell)
			self.update_cell(cell)

			if cell in self.cells:
				#remove visited cell from the overall cells list
				self.cells.remove(cell)


	def move(self, cell, direction):

		if self.path_directions != []:
			prev = self.opposites[self.path_directions[-1]]
			direction.remove(prev)

		#print(direction, cell)

		if cell[0] == 0:
			#print("here1",direction)
			if 't' in direction:
				direction.remove('t')
		if cell[1] == 0:
			#print("here2",direction)
			if 'l' in direction:
				direction.remove('l')
		if cell[0] == self.width-1:
			#print("here3",direction)
			if 'b' in direction:
				direction.remove('b')
		if cell[1] == self.width-1:
			#print("here4",direction)
			if 'r' in direction:
				direction.remove('r')

		di = random.choice(direction)
		self.path_directions.append(di)

		#print(direction, di, cell)

		if di == 'l':
			cell = (cell[0], cell[1]-1)
		elif di == 'r':
			cell = (cell[0], cell[1]+1)
		elif di == 't':
			cell = (cell[0]-1, cell[1])
		elif di == 'b':
			cell = (cell[0]+1, cell[1])

		return cell


	def create_path(self):

		path = []

		self.current_cell = self.choose_cell()
		#print(self.current_cell)

		while True:
			if self.current_cell not in self.visited:
				if self.current_cell not in path:

					# update path before re-assigning value to current_cell
					path.append(self.current_cell)

					direction = self.direction[:]
					self.current_cell = self.move(self.current_cell, direction)
					#print("Here", self.current_cell)
					#print(self.path)

				else:
					return 0
			else:
				return path


	def maze(self):

		# starting cell
		self.mark_visited([self.choose_cell()])

		while True:
			if self.cells != []:
				temp_path = self.create_path()
				if temp_path != 0:
					self.mark_visited(temp_path)
					print(self.maze_array)
					#break
				else:
					continue
			else:
				break


maze = Maze(6)
maze.maze()