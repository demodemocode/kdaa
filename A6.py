import queue 

class Node:
	def __init__(self, student_id, club_id, parent, path_cost, assigned):
		self.student_id = student_id
		self.club_id = club_id
		self.parent = parent
		self.path_cost = path_cost
		self.assigned = assigned.copy()
		
	def __lt__(self,other):
		return self.path_cost < other.path_cost
		
def calculate_cost(cost_matrix, student_id, club_id, assigned):
	cost = 0
	available = [True] * N
	
	for i in range(student_id + 1, N):
		min_val, min_index = float('inf'), -1
		for j in range(N):
			if not assigned[j] and available[j] and cost_matrix[i][j] < min_val:
				min_val = cost_matrix[i][j]
				min_index = j
			
		if min_index == -1:
			cost = float('inf')
			break
		
		cost += min_val
		available[min_index] = False
	
	return cost 


def find_min_cost(cost_matrix, N):
	
	pq = queue.PriorityQueue()
	assigned = [False] * N
	
	root = Node(-1, -1, None, 0, assigned)
	pq.put((root.path_cost, root))
	
	best_solution = (float('inf'), None)
	
	while not pq.empty():
		_, min_node = pq.get()
		i = min_node.student_id + 1
		
		if i == N :
			if min_node.path_cost < best_solution[0]:
				best_solution = (min_node.path_cost, min_node)
			continue
		
		if min_node.path_cost >= best_solution[0]:
			continue # prune branch
		
		for j in range(N):
			if not min_node.assigned[j]:
				assigned_copy = min_node.assigned.copy()
				assigned_copy[j] = True
				child = Node(i, j, min_node, min_node.path_cost + cost_matrix[i][j], assigned_copy)
				pq.put((child.path_cost + calculate_cost(cost_matrix, i, j, child.assigned), child))
		
	return best_solution[0], best_solution[1] 
	
def print_assignments(min_node):
	assignments = []
	while min_node is not None:
		if min_node.student_id >= 0 and min_node.club_id >= 0:
			assignments.append(f"student {min_node.student_id + 1} assigned to {min_node.club_id + 1}")
		min_node = min_node.parent
	
	assignments.reverse()
	return assignments
		

N = int(input("Enter number of student/club: "))
cost_matrix = []

print("Entre cost matrix")
for _ in range(N):
	row = list(map(int, input().split()))
	cost_matrix.append(row)

optimal_cost, best_solution = find_min_cost(cost_matrix, N)

assignments = print_assignments(best_solution)

print(f"Optimal cost is {optimal_cost}")

for assignment in assignments:
	print(assignment)



	
