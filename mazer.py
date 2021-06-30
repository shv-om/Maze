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
		self.directn = ['l', 'r', 't', 'b']
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
		i = 1
		for cell in temp_cells:
			# update the visited list
			self.visited.append(cell)
			#print(cell)
			self.update_cell(cell, i)
			i += 1

			if cell in self.cells:
				#remove visited cell from the overall cells list
				self.cells.remove(cell)


	def move(self, cell, directn):

		if self.path_directions != []:
			prev = self.opposites[self.path_directions[-1]]
			directn.remove(prev)

		if cell[0] == 0:
			if 't' in directn:
				directn.remove('t')
		if cell[1] == 0:
			if 'l' in directn:
				directn.remove('l')
		if cell[0] == self.width-1:
			if 'b' in directn:
				directn.remove('b')
		if cell[1] == self.width-1:
			if 'r' in directn:
				directn.remove('r')

		di = random.choice(directn)

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
					directn = self.directn[:]
					# update path before re-assigning value to current_cell
					path.append(self.current_cell)

					self.current_cell = self.move(self.current_cell, directn)
					path.append(self.current_cell)

				else:
					return 0
			else:
				return path


	def maze(self):

		# starting cell
		initial_cell = self.choose_cell()
		self.mark_visited([initial_cell])
		self.path.append([initial_cell])

		while True:
			if self.cells != []:
				temp_path = self.create_path()
				if temp_path != 0:
					self.mark_visited(temp_path)
					self.path.append(temp_path)

					#break
				else:
					continue
			else:
				break


		return self.path


class Draw:
	
	def __init__(self, points, tunnel='15', scale=20):
		self.points = points

		self.scale = scale

		self.screen = turtle.Screen()
		self.screen.setworldcoordinates(-1, -1, self.screen.window_width() - 1, self.screen.window_height() - 1)

		self.cursor = turtle.Turtle()
		turtle.bgcolor('black')
		self.cursor.color('white')
		self.cursor.hideturtle()
		self.cursor.pensize(tunnel)
		self.cursor.speed(0)



	def move_cursor(self):

		for cell_list in self.points:
			
			self.cursor.up()
			cell1 = cell_list[0]
			self.cursor.goto((cell1[0]*scale, cell1[1]*scale))

			for cell in cell_list:
				self.cursor.down()
				self.cursor.goto((cell[0]*scale, cell[1]*scale))



size = int(input("Enter Maze Size: "))
print("\n***--- Note: For good result tunnel size must be smaller than scale size ---***\n")
tunnel = input("Enter the size (tunnel size): ")
scale = int(input("Enter Scale (distance between tunnel): "))

maze = Maze(size)
l = maze.maze()

drw = Draw(l, tunnel, scale)
drw.move_cursor()
input()