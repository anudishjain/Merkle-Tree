'''

Merkle Root Implementation in Python, the script assumes data is contained in csv file and each line in the file
represents a new transaction,

Currently supports calculating the merkle root of a large data set contained inside the csv file 

'''
from csv import *
from hashlib import * 

filePath = "example.csv"
''' absolute or relative path to the csv file containing the transactions or data '''


fileOpen = open(filePath, 'rU')
''' opening the file for reading in Universal NewLine (rU) '''

fileReader = reader(fileOpen)
''' initializing the CSV Reader for traversing data inside the csv file '''

storeHash = []

for row in fileReader :

	for tnx in row :

		currentItem = str(tnx)
		storeHash.append(sha256(currentItem).hexdigest())


if (len(storeHash) % 2 != 0) :
	storeHash.append(storeHash[-1])


while(len(storeHash)> 1) : 

	j = 0;

	for i in range(0, len(storeHash) - 1) : 

		storeHash[j] = sha256(str(storeHash[i] + storeHash[i+1])).hexdigest()
		
		i += 2
		j += 1


	lastDelete = i - j;
	del storeHash[-lastDelete:];


merkleFile = open('merkle.csv', 'wb')
write = writer(merkleFile)
write.writerow(storeHash)