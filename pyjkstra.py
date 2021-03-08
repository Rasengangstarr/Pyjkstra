def listToGraph(l):
    nodes = {}
    
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

            if x > 0 and y < len(l) and l[y+1][x-1]:
               associated_nodes[(str(x-1)+','+str(y+1))] = 1 
    
            nodes[node_key] = associated_nodes

    return nodes


test_list = [[1,1,1],[1,1,1],[1,1,1]]

print(listToGraph(test_list))
