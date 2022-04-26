import networkx as nx
import csv

#####################################################
##      Generating PageRank from Hypergraph        ##
#####################################################

# same as pageRankSimple, but instead of taking the simple graph, we compute pagerank in Hypergraphs
# So in this case, instead of stations, trains are ranked as pages in network

G = nx.Graph()

file = open('trainWeights.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')

TrainWeight = dict()

flag = True
for x in reader:
    if(len(x)!=0):
        if flag:
            flag = not flag
        else:
            TrainWeight[x[0]] = float(x[2])
            G.add_node(x[0])

file.close()
pageRank = nx.pagerank(G, personalization=TrainWeight)

pr_list = []

for x in pageRank:
    pr_list.append(["'" + x + "'", pageRank[x]])

outputfile = open("pageRankHyper.csv", 'w')
print("Output stored in pageRankHyper.csv")
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(pr_list)