# Merkle-Tree 🌲

Python Script to calculate Merkle Root of a CSV File Input.

A Merkle Tree is a complete binary tree which is used by Cryptocurrency SPV Wallets.

Simple Payment Verification (SPV) is a technique described in Satoshi Nakamoto's paper. SPV allows a lightweight client to verify that a transaction is included in the Bitcoin blockchain, without downloading the entire blockchain.

By using a merkle tree, one can validate a large data set contained inside the tree by just comparing the merkle root / root node of the tree.

This script assumes the input data is in the form of CSV File, and saves the finally calculated merkle root for the user in another CSV File.

A Merkle Tree can look like this : 


![alt text](https://cdn-images-1.medium.com/max/1600/1*UrjiK3IjdbgoV2dyKRvAGQ.png)


The data is stored in the leaf nodes and we bubble up from botton to top by calculating the hash of each leaf node.

At the end we are left with a single merkle root capable of validating the whole data set with just a single hash string of 32 bytes.

# Applications

- Multiple Vendor Systems can use merkle trees to validate the copy of transactions / data that each individual holds and thus instead of traversing the file to compare values, they can simply verify the merkle root that they calculated.

- Merkle Trees reduce the number of computations required for verification of a single component in a large data set as once the tree is created it needs a small amount of information (1 hash per level of the tree) to calculate and reach the valid merkle root. As shown, 

![alt text](https://i.stack.imgur.com/2Ep7y.png)

# Performance of the Script

For a CSV File with 1000 rows it takes 1.1 sec to get merkle root.
(The script doesn't support validation currently, just merkle root calculation using sha256 hashing)

