import csv

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
        if not x[0] in Trains_list:
            Trains_list.append(x[0])
            Train_to_Label[x[0]] = x[1]
            Train_to_Station[x[0]] = []
        Train_to_Distance[x[0]] = int(x[7])
        Train_to_Station[x[0]].append(x[3])
file.close()

edges_list = []


for i in range(0, len(Trains_list)-1):
    for j in range(i+1, len(Trains_list)):
        c = set(Train_to_Station[Trains_list[i]]).intersection(
            set(Train_to_Station[Trains_list[j]]))
        diff1 = abs(len(c.intersection(
            Train_to_Station[Trains_list[i]])) - len(Train_to_Station[Trains_list[i]]))
        diff2 = abs(len(c.intersection(
            Train_to_Station[Trains_list[j]])) - len(Train_to_Station[Trains_list[j]]))
        f1 = len(c)/float(len(Train_to_Station[Trains_list[i]]))
        f2 = len(c)/float(len(Train_to_Station[Trains_list[j]]))
        final = (f1 + f2)/2.0
        if bool(c) and (diff1 > 2) and (diff2 > 2) and (abs(int(Trains_list[i]) - int(Trains_list[j])) > 2):
            edges_list.append(["'" + Trains_list[i] + "'",
                              "'" + Trains_list[j] + "'", final])

outputfile = open("hyperedges.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(edges_list)

nodes_list = []

for x in Trains_list:
    nodes_list.append(["'" + x + "'", Train_to_Label[x], Train_to_Distance[x]])

outputfile = open("hypernodes.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(nodes_list)
