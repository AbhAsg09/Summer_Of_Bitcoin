**This is my solution for the problem question by Summer of Bitcoin**
I have chosen Python as the language to solve this problem as CSV file management is easy in Python.
I have used **Pandas** library for it's functionality.
The solution is stored in the **"Solution Block"** folder as a .txt file named **"block_file.txt"**. 

To run the code, download it and in line 4, add the path for the file destination inside the **read_csv**  function.

## Approach

 - Take the **"mempool.csv"** file as a variable named **"dataframe"** in read mode. 
 - In the dataframe variable, fill all the empty cells in **"parents"** column as **"NULL"**.
 - Define a function **"find_txs"**:
	 - This function is used to find whether a given parent/parents are valid or not. If they are valid then the function should return 0, else they are bad_parents.
 - Define a function **"get_badParents"**:
	  - This function returns a list with indexes of the bad parents.
 - Define a dictionary **"idx2parents"** which is a "index" to "parent-transaction-id" mapping, which we use as a utility.
 - In a while loop we iteratively keep on deleting the **'bad parents'** until the dataset is free of them.
 - We sort the entire  dataframe with respect **'fee**' column in descending order.
 - Define a function **result**:
	 - Here we maximize the **weight** and **fee**.
	 - The function returns a list of transaction ids which maximize the **'fee'** for the weight closest possible to, but not more than 4 million.
 - We store the list returned by function **result** in **"result_ls"** and store it in a text file named **"block_file.txt"** which stores the transaction id of the transactions to be included in a block, separated by newline. 

 

 

 
