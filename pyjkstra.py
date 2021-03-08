def listToGraph(l):
    nodes = {}
    keys = [] 
    for y in range(len(l)):
        for x in range(len(l[0])):
            associated_nodes = {} 
            node_key = str(x)+','+str(y)
            if x > 0 and l[y][x-1] != 0:
               associated_nodes[(str(x-1)+','+str(y))] = 1

            if y > 0 and l[y-1][x] != 0:
               associated_nodes[(str(y-1)+','+str(y))] = 1 

            if x > 0 and y > 0 and l[y-1][x-1] != 0:
               associated_nodes[(str(x-1)+','+str(y-1))] = 1 

            if x < len(l[0]) - 1 and l[y][x+1] != 0:
               associated_nodes[(str(x+1)+','+str(y))] = 1 

            if y < len(l) - 1 and l[y+1][x] != 0:
               associated_nodes[(str(x)+','+str(y+1))] = 1 

            if x < len(l[0]) - 1 and y < len(l) - 1 and l[y+1][x+1] != 0:
               associated_nodes[(str(x+1)+','+str(y+1))] = 1 

            if x < len(l[0]) - 1 and y > 0 and l[y-1][x+1] != 0:
               associated_nodes[(str(x+1)+','+str(y-1))] = 1 

            if x > 0 and y < len(l) - 1 and l[y+1][x-1]:
               associated_nodes[(str(x-1)+','+str(y+1))] = 1 
    
            nodes[node_key] = associated_nodes
            keys.append(node_key)
    keys = tuple(keys) 
    return (nodes, keys)


#fully YEETED from https://www.pythonpool.com/dijkstras-algorithm-python/
def dijkstra(nodes, distances):
    # These are all the nodes which have not been visited yet
    unvisited = {node: None for node in nodes}
    # It will store the shortest distance from one node to another
    visited = {}
    current = '0,0'
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for 
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # Till now the shortest distance between the source node and target node 
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited


test_list = [[1,1,1],[1,1,1],[1,1,1]]
(distances, keys) = listToGraph(test_list)
print(dijkstra(keys, distances))
