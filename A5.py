N = int(input("Enter Board size: "))
x = int(input("starting row: "))
y = int(input("starting col: "))

board = [[-1 for i in range(N)] for i in range(N)]

def issafe(board,x,y):
	if x >= 0 and x < N and y >= 0 and y < N and board[x][y] == -1:
		return True
	return False
	
def print_board():
	for i in range(N):
		for j in range(N):
			print(board[i][j],end = " ")
		print()	

def solvKTUtil(board,x,y,mov_x,mov_y,pos):
	if(pos == (N**2)):
		return True
	
	for i in range(8):
		new_x = x + mov_x[i]
		new_y = y + mov_y[i]
		
		if(issafe(board,new_x,new_y)):
			board[new_x][new_y] = pos
			if(solvKTUtil(board,new_x,new_y,mov_x,mov_y,pos + 1)):
				return True
			board[new_x][new_y] = -1
	
	return False

def solveKT():
	mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
	mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
	board[x][y] = 0
	if(solvKTUtil(board,x,y,mov_x,mov_y,1)):
		print(print_board())
	else:
		print("solution does not exist")

	
	
	
solveKT()
