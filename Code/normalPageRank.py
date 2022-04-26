import networkx as nx
import csv

G = nx.Graph()

file = open('stationWeights.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')

StationWeight = {}

flag = True
for x in reader:
    if flag:
        flag = not flag
    else:
        StationWeight[x[0]] = int(x[2])
        G.add_node(x[0])

file.close()
pageRank = nx.pagerank(G, personalization=StationWeight)

pr_list = []

for x in pageRank:
    pr_list.append([x, pageRank[x]])

outputfile = open("pageRankSimple.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(pr_list)
