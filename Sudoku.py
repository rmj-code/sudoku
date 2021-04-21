# grid = [[4,0,7,0,0,9,0,0,0],
# 		[6,0,5,0,0,7,0,2,0],
# 		[0,0,0,0,0,0,8,0,3],
# 		[5,4,0,7,6,0,3,0,9],
# 		[3,0,8,2,0,4,5,0,7],
# 		[9,0,6,0,1,3,0,4,8],
# 		[2,0,3,0,0,0,0,0,0],
# 		[0,9,0,3,0,0,1,0,2],
# 		[0,0,0,9,0,0,4,0,5],
# ]

# worlds hardest sudoku
# grid = [[8,0,0,0,0,0,0,0,0],
# 		[0,0,3,6,0,0,0,0,0],
# 		[0,7,0,0,9,0,2,0,0],
# 		[0,5,0,0,0,7,0,0,0],
# 		[0,0,0,0,4,5,7,0,0],
# 		[0,0,0,1,0,0,0,3,0],
# 		[0,0,1,0,0,0,0,6,8],
# 		[0,0,8,5,0,0,0,1,0],
# 		[0,9,0,0,0,0,4,0,0],
# ]


grid = [[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,1,0,0,0,0,0,0],
		[0,0,0,0,0,0,2,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
]

def print_board(grid):
	for i_row in range(len(grid)):
		if i_row % 3 == 0 and i_row != 0:
			print("- " * 12)

		for i_col in range(len(grid[0])):
			if i_col % 3 == 0 and i_col != 0:
				print(" | ", end="")

			if i_col == 8:
				print(grid[i_row][i_col])

			else:
				print(str(grid[i_row][i_col]) + " ", end="")


def find_empty(grid):
	for i_row in range(len(grid)):
		for i_col in range(len(grid[0])):
			if grid[i_row][i_col] == 0:
				return i_row, i_col


def solve(grid):
	empty_cell = find_empty(grid)

	if not empty_cell:
		return True		# Solved!
	else:
		row, col = empty_cell

		# loop through 1-9 to try 
		for i_num in range(1,10):
			if is_valid(grid, i_num, (row,col)):
				grid[row][col] = i_num

				if solve(grid):	# recursion
					return True

				grid[row][col] = 0

		return False






def is_valid(grid, num,row_col):
	row_list = grid[row_col[0]]					# Get Row as list
	col_list = list(zip(*grid))[row_col[1]]		# Get Col as list
	mini_grid_r = (row_col[0]//3) * 3	# Get mini grid (row,col)  - x//3 == int(x/3)
	mini_grid_c = (row_col[1]//3) * 3	# Get mini grid (row,col)
	mini_grid = list(rws[mini_grid_c:mini_grid_c+3] for rws in grid[mini_grid_r:mini_grid_r+3])

	if (num in row_list):	# check if in rows
		return False			# f"Exists in row {row_col[0]}: {row_list}"
	elif (num in col_list):	# check if in columns
		return False			# f"Exists in col {row_col[1]}: {col_list}"
	elif (num in list(x for rw in mini_grid for x in rw)):
		return False			# f"Exists in mini_grid {mini_grid}"
	else:
		return True



print_board(grid)
print("*" * 30)
solve(grid)
print_board(grid)

