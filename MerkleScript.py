'''

Merkle Root Implementation in Python, the script assumes data is contained in csv file and each line in the file
represents a new transaction,

Currently supports calculating the merkle root of a large data set contained inside the csv file,

next feature, how to validate a single data point without traversing the whole file

'''

from csv import *
from hashlib import * 

filePath = "example.csv"
# absolute or relative path to the csv file containing the transactions or data '''


fileOpen = open(filePath, 'rU')
# opening the file for reading in Universal NewLine (rU) 

fileReader = reader(fileOpen)
# initializing the CSV Reader for traversing data inside the csv file

storeHash = []
# list to store the hashes as they are calculated

for row in fileReader :

	for tnx in row :

		currentItem = str(tnx).encode("utf-8")
		storeHash.append(sha256(currentItem).hexdigest())

		# calculate hash row wise and save them in the storeHash


if (len(storeHash) % 2 != 0) :
	storeHash.append(storeHash[-1])

	'''

	Merkle Tree is a complete binary tree, 
	so if the number of inputs from CSV are odd, we duplicate the last record's hash in the list

	'''


while (len(storeHash)> 1) : 
	# we run the loop till we don't get a single hash

	j = 0;

	for i in range(0, len(storeHash) - 1) : 

		storeHash[j] = sha256(str(storeHash[i] + storeHash[i+1]).encode("utf-8")).hexdigest()
		# hash of the i th leaf and i + 1 th leaf are concatenated
		# to find the hash parent to the both
		
		i += 2
		j += 1


	lastDelete = i - j;

	del storeHash[-lastDelete:];
	# as we now have the hash to the upper level of the tree, we delete the extra space in the array.
	# in each iteration of this loop the size of the storeHash list is halved.


merkleFile = open('merkle.csv', 'w')
# create the file for saving the merkle root

write = writer(merkleFile)

write.writerow(storeHash)
# write to the file in simple text mode
