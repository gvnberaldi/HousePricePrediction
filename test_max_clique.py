#! /usr/bin/python3




def decide_clique(graph: list[list[int]] , set_nodes : list[int] ):

    for i in set_nodes:
        for j in set_nodes:
            if i != j and graph[i][j] == 0:
                return False
    
    return True

def decide_maximal_clique(graph: list[list] , set_nodes : list[int]):
    
    if not decide_clique(graph=graph, set_nodes=set_nodes):
        return False
    
    for i in range(len(graph)):
        if i not in set_nodes:
            b = True
            for j in set_nodes:
                if graph[i][j] == 0:
                    b = False
            if b :
                return False
    
    return True


def function_maximal_clique(graph: list[list], n: int) -> list[list[int]]:
    
    if(len(graph) < n or n <= 0):
        return None 

    res = []
    
    maximal_clique = [ i for i in range(n)]

    i = n - 1
    while( maximal_clique[0] < len(graph) - n + 1):

        if i == len(maximal_clique) - 1 and decide_maximal_clique(graph=graph, set_nodes=maximal_clique):
             res.append(maximal_clique.copy())
        
        # if i == n - 1:
        #     print(maximal_clique)
        
        
        maximal_clique[i] += 1
        if maximal_clique[i] < (len(graph) - n + 1 + i):
            # Can increment all counters up to n - 1
            for j in range(i+1,n):
                maximal_clique[j] = maximal_clique[j-1] + 1
            i = n - 1 
        else:
            i -= 1
            
        
    return res
        

def function_maximal_clique_all(graph: list[list]) -> list[list[int]]:
    
    n = len(graph)

    res = []
    while n > 0 :
        resi = function_maximal_clique(graph=graph, n=n)
        n -= 1
        if(resi != []):
            res.append(resi)

    return res
        
        









graph = [ [ 0 for _ in range(7) ] for _ in range(7)  ]

graph[0][1] = 1
graph[0][2] = 1
# graph[0][3] = 1
graph[1][2] = 1
graph[1][3] = 1
graph[1][6] = 1
graph[2][3] = 1
graph[4][5] = 1
graph[4][6] = 1
graph[5][6] = 1


for i in range(len(graph)):
    for j in range(i+1, len(graph[i])):
        if graph[i][j] == 1:
            graph[j][i] = 1

for row in graph:
    print(row)

print("-"*100)

maximal_cliques = function_maximal_clique_all(graph=graph)

for clique in maximal_cliques:
    print(clique)