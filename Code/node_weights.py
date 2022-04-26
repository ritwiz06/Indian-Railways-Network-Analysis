import csv

########################################
##      Generating Train_weights      ##
########################################

file = open('train_data.csv', 'r')
reader = csv.reader(file, skipinitialspace=True, quotechar="'", delimiter=',')
# [Train No., train Name, islno, station Code, Station Name, Arrival time,
#    Departure time, Distance, Source Station Code, source Station Name, Destination station Code, Destination Station Name]

Trains_list = {} # dictionary : {}
Station_to_Train = {} # dictionary : {station_code : [train_no.]}
Train_to_name = {} # dictionary : {station_code: [train_nos]}
Train_to_station = {} # dictionary : {Train_no: [station_codes]}

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

outputfile = open("stationWeights.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(nodes_list)

weights_list = []

for x in Train_to_station:
    weights_list.append(["'" + x + "'", Train_to_name[x], len(Train_to_station[x])])

outputfile = open("trainWeights.csv", 'w')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE, delimiter=',')
wr.writerows(weights_list)

#trainWeight.csv : [train_code, train name, no. of stations they pass through]

#stationWeights.csv : [station_code, weight]

print("Output saved in trainWeights.csv & stationWeights.csv")