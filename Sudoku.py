
grid = [[0,2,3,4,5,6,7,8,9],
		[2,3,4,5,6,7,8,9,1],
		[3,3,4,5,6,7,8,9,1],
		[4,3,4,5,6,7,8,9,1],
		[5,3,4,5,6,7,8,9,1],
		[6,3,4,5,6,7,8,9,1],
		[7,3,4,5,6,7,8,9,1],
		[8,3,4,5,6,7,8,9,1],
		[9,3,4,5,6,7,8,9,1]]

def print_board(bo):
	pass

def find_empty(bo):
	pass

def solve(bo):
	pass






def is_valid(num,grid,row_n,col_n):
	row_list = grid[row_n]					# Get Row as list
	col_list = list(zip(*grid))[col_n]		# Get Col as list
	mini_grid_r = int(row_n/3)*3	# Get mini grid (row,col)
	mini_grid_c = int(col_n/3)*3	# Get mini grid (row,col)
	mini_grid = list(rws[mini_grid_c:mini_grid_c+3] for rws in grid[mini_grid_r:mini_grid_r+3])

	print("num: ",num)
	print("row_list: ",row_list)
	print("col_list: ",col_list)
	print("mini_grid_r: ",mini_grid_r)
	print("mini_grid_c: ",mini_grid_c)
	print("mini_grid: ",mini_grid)




	if (num in row_list):	# check if in rows
		return f"Exists in row {row_n}: {row_list}"
	elif (num in col_list):	# check if in columns
		return f"Exists in col {col_n}: {col_list}"
	elif (num in list(x for rw in mini_grid for x in rw)):
		return f"Exists in mini_grid {mini_grid}"
	else:
		return "Free"

print (check_num(num=4,grid=grid, row_n=0, col_n=0))

# def check_row(num, row_list)
# 	if (num in row_list):
# 		return "Exists"
# 	else:
# 		return "Not In"

# print(check_row(1))
# print(grid)
# print("-"*100)
# print(*grid)
# print("-"*200)
# print(list(zip(*grid)))