# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path_trace={str(init):[]}
    
    
    
    current=init
    openned=[]
    closed=[]
    
    print('check', current!=goal)
    while current!=goal :
        print(current)
        adjacent=[[current[0]+item[0],current[1]+item[1]] for item in delta if current[0]+item[0]>=0 and current[0]+item[0]<len(grid) and current[1]+item[1]>=0 and current[1]+item[1]<len(grid[0]) and grid[current[0]+item[0]][current[1]+item[1]]==0]
        
        openned=openned+[item for item in adjacent if item not in openned and item not in closed]
        closed.append(current)
        if len(openned)>0:
            current=openned.pop()
        else:
            return "fail"
        
            

        path_trace[str(current)]=path_trace[str(closed[-1])]+[current]
        print(path_trace)

    if current==goal:
        
        path= [len(path_trace[str(goal)]), goal[0], goal[1]]
        return path

pathT=search(grid,init,goal,cost)
print(pathT)
# for key in pathT.keys():
#     print(key, len(pathT[key]))
