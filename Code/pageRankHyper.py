import networkx as nx
import csv

G = nx.Graph()

file = open('trainWeights.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')

TrainWeight = {}

flag = True
for x in reader:
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
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(pr_list)
