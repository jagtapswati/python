graph={
 '0':['1','4'],
 '1':['2','3','4'],
 '2':['1','3'],
 '3':['1','2'],
 '4':['0','1'],
    
}

visited=set()       # set to keep track of visited nodes of graph.

def dfs(visited,graph,node):        #function for dfs
     if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            
#driver code 
print("following is the depth-first search")
dfs(visited,graph,'0')
            