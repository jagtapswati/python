graph={
 '0':['1','4'],
 '1':['2','3','4'],
 '2':['1','3'],
 '3':['1','2'],
 '4':['0','1'],
 
        
}

visited =[]             # list of visited nodes
queue =[]               # initialize queue

def bfs (visited,graph,node):       #functon for bfs 
    
    visited.append(node)
    queue.append(node)
    
    # creating looop to while queue : visit each node
    m =queue.pop(0)
    print(m, end=" ")
    for neighbour in graph [m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
            
# driver code             
print("following is the breadth first search")
bfs(visited,graph,'0')      #function calling






