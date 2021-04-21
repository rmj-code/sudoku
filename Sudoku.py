
grid = [[1,2,3,4,5,6,7,8,9],
		[2,3,4,5,6,7,8,9,1],
		[3,3,4,5,6,7,8,9,1],
		[4,3,4,0,6,7,8,9,1],
		[5,3,4,5,6,7,8,9,1],
		[6,3,4,5,6,7,8,9,1],
		[7,3,4,5,6,7,8,9,1],
		[8,3,4,5,6,7,8,9,1],
		[9,3,4,5,6,7,8,9,1]]

def print_board(bo):
	for i_row in range(len(bo)):
		if i_row % 3 == 0 and i_row != 0:
			print("- " * 12)

		for i_col in range(len(bo[0])):
			if i_col % 3 == 0 and i_col != 0:
				print(" | ", end="")

			if i_col == 8:
				print(bo[i_row][i_col])

			else:
				print(str(bo[i_row][i_col]) + " ", end="")


def find_empty(bo):
	for i_row in range(len(bo)):
		for i_col in range(len(bo[0])):
			if bo[i_row][i_col] == 0:
				return i_row, i_col

print(find_empty(grid))

def solve(bo):
	pass






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



print_board(bo=grid)

