import networkx as nx
import csv

#####################################
##      Generating PageRank        ##
#####################################

G = nx.Graph()

file = open('stationWeights.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')

StationWeight = {} # dictionary : {station_name : station_wt}

flag = True
for x in reader:
    if(len(x)!=0):
        if flag:
            flag = not flag
        else:
            StationWeight[x[0]] = int(x[1])
            G.add_node(x[0])

file.close()
pageRank = nx.pagerank(G, personalization=StationWeight)

"""
Returns the PageRank of the nodes in the graph.
PageRank computes a ranking of the nodes in the graph G based on
the structure of the incoming links. It was originally designed as
an algorithm to rank web pages.
"""

pr_list = []

for x in pageRank:
    pr_list.append([x, pageRank[x]])

outputfile = open("pageRankSimple.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(pr_list)

# pageRankSimple.py : [station, rank in network]

print("Output saved in pageRankSimple.csv")