import csv

file = open(
    'train_data.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')

Trains_list = {}
Station_to_Train = {}
Train_to_name = {}
Train_to_station = {}

flag = True
for x in reader:
    if flag:
        flag = not flag
    else:
        if not x[0] in Train_to_name:
            Train_to_name[x[0]] = x[1]
            Train_to_station[x[0]] = []
        if not x[3] in Station_to_Train:
            Station_to_Train[x[3]] = []
        Station_to_Train[x[3]].append(x[0])
        Train_to_station[x[0]].append(x[3])
file.close()

nodes_list = []

for x in Station_to_Train:
    nodes_list.append([x, 10*len(Station_to_Train[x])])

outputfile = open(
    "stationWeights.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(nodes_list)

# for x in Station_to_Train:
# 	weight = 10.0/len(Station_to_Train[x])
# 	for y in Station_to_Train[x]:
# 		if not y in Trains_list:
# 			Trains_list[y] = weight
# 		if weight > Trains_list[y]:
# 			Trains_list[y] = weight

weights_list = []

for x in Train_to_station:
    weights_list.append(
        ["'" + x + "'", Train_to_name[x], len(Train_to_station[x])])

outputfile = open(
    "trainWeights.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(weights_list)

print("Output saved in trainWeights.csv")