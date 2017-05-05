import sys
import community
import networkx as nx
import itertools
#import matplotlib.pyplot as plt
#%matplotlib inline

def read_dimacs_format(lines):
    number_of_variables = None
    number_of_clauses = None
    
    clauses = []

    for line in lines:
        tokens = line.split()
        if not len(tokens) or tokens[0] == 'c':
            continue
	elif tokens[0] == 'p' and tokens[1] == 'cnf':
            number_of_variables = int(tokens[2])
            number_of_clauses = int(tokens[3])
        elif tokens[-1] == '0':
            clause = [int(i) for i in tokens[:-1]]
            clauses.append(clause)
    return number_of_variables, number_of_clauses, tuple(clauses)

def build_graph(G, sat_instance):
    '''
    Construct Variable Incidence Graph 
    '''
    for clause in sat_instance:
        if len(clause) > 1:
            weight = 1.0 / (len(clause) - 1)
            for combination in itertools.combinations(clause, 2):
                a=abs(combination[0])
                b=abs(combination[1])
                if G.has_edge(a, b):
                    G[a][b]['weight']+=weight
                else:
                    G.add_edge(a, b, weight=weight)

if __name__ == '__main__':
    filename = sys.argv[1]
    
    content = []
    with open(filename, "r") as f:
        content = f.readlines()

    number_of_variables, number_of_clauses, sat_instance = read_dimacs_format(content)
    G = nx.Graph()
    build_graph(G, sat_instance)
    


    samplesize = nx.number_of_nodes(G) / 50
    centralit = nx.betweenness_centrality(G, k=samplesize, normalized=True)



    filename = sys.argv[1]
    filename = filename+'.centralityscores-n-502'
    f = open(filename, 'w')
    for k in centralit.keys():
        f.write(str(centralit[k]))
        f.write('\n')

    filename = sys.argv[1]
    filename = filename+'.centrality-n-502'
    f = open(filename, 'w')
    for key, value in sorted(centralit.iteritems(), key=lambda (k,v): (v,k)):
        f.write(str(key-1))
        f.write(' ')
        f.write(str(value))
        f.write('\n')


    
