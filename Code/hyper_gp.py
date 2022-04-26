import csv

#####################################
##      Generating Hypergraph      ##
#####################################

# traindata.csv has details of 69000 train and their journeys
# [Train No., train Name, islno, station Code, Station Name, Arrival time,
#    Departure time, Distance, Source Station Code, source Station Name, Destination station Code, Destination Station Name]

file = open('train_data.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')

Trains_list = []
Train_to_Station = {}
Train_to_Label = {}
Train_to_Distance = {}
Station_to_Train = {}

flag = True
for x in reader:
    if flag:
        flag = not flag
    else:
        if not x[0] in Trains_list: # if this train has already not been recorded
            Trains_list.append(x[0]) # add the train no. to list of trains
            Train_to_Label[x[0]] = x[1] # dictionary : {train_no. : train_name}
            Train_to_Station[x[0]] = [] # empty list for the key : train_no
        Train_to_Distance[x[0]] = int(x[7]) # distance to the destination station
        Train_to_Station[x[0]].append(x[3]) # dictionary : {Train_no : station code}
file.close()

edges_list = []


for i in range(0, len(Trains_list)-1):
    for j in range(i+1, len(Trains_list)):
        # c = finding common trains from station i to station j
        c = set(Train_to_Station[Trains_list[i]]).intersection(set(Train_to_Station[Trains_list[j]]))

        # diff1 = difference in number of trains common between `station c` and `station i` AND `station i`
        diff1 = abs(len(c.intersection(Train_to_Station[Trains_list[i]])) - len(Train_to_Station[Trains_list[i]]))
        # diff2 = difference in number of trains common between `station c` and `station j` AND `station j`
        diff2 = abs(len(c.intersection(Train_to_Station[Trains_list[j]])) - len(Train_to_Station[Trains_list[j]]))

        f1 = len(c)/float(len(Train_to_Station[Trains_list[i]]))
        f2 = len(c)/float(len(Train_to_Station[Trains_list[j]]))
        final = (f1 + f2)/2.0

        if bool(c) and (diff1 > 2) and (diff2 > 2) and (abs(int(Trains_list[i]) - int(Trains_list[j])) > 2):
            edges_list.append(["'" + Trains_list[i] + "'", "'" + Trains_list[j] + "'", final])

outputfile = open("hyperedges.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(edges_list)

nodes_list = []

for x in Trains_list:
    nodes_list.append(["'" + x + "'", Train_to_Label[x], Train_to_Distance[x]])

outputfile = open("hypernodes.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(nodes_list)

# in a regular graph, nodes are stations, and edges are trains connecting them
# in HYPERGRAPHS, the edges can connect more than 2 nodes, so they weight of the edge taken here is the average of stations they connect
#hyperedges.csv : [Train_i, Train_j, average of stations they connect]

#hypernodes.csv : [Train_no., Train_name, Train_distance]

print("Output saved in hypernodes.csv & hyperedges.csv")