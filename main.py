import pandas as pd

# !!pls change the path to where you have stored you .csv file
dataframe = pd.read_csv('mempool.csv')
dataframe['parents '] = dataframe['parents '].fillna('NULL')

tx_id = list(dataframe['tx_id']) # List of transaction ids

# This function is used to find whether a given parent/parents are valid or not
# if they are valid then the function should return 0, else they are bad_parents
def find_txs(k1, v1):
    correct_txns = {}
    ps = [i for i in v1]
    for i in range(k1):
        if tx_id[i] in ps:
            ps.remove(tx_id[i])
    return len(ps)


# This function returns a list with indexes of the bad parents
def get_badParents(parents):
    li_parents = []
    for i in parents:
        if i != 'NULL' and ';' in i:
            x=i.split(';')
        else:
            x = [i]
        li_parents.append(x)

    idx2parents = {}  # this is a "index" to "parent-transaction-id" mapping, which we use as a utility
    for idx in range(len(li_parents)):
        curr = li_parents[idx]
        if curr[0] != 'NULL':
            idx2parents[idx] = curr

    # getting the valid parent ids
    list_valid_idxs = []
    for key, value in idx2parents.items():
        n1 = find_txs(key, value)
        if n1 == 0:
            list_valid_idxs.append(key)

    # Getting the bad/invalid parent ids
    bad_parents = []
    for key, values in idx2parents.items():
        if key not in list_valid_idxs:
            bad_parents.append(key)

    return bad_parents


li_parents = list(dataframe['parents '])
bad_parents = get_badParents(li_parents)

# we iteratively keep on getting the 'bad parents' until the dataset is free of them
# After it's done we can move on with the maximization of transaction fees
while True:
    dataframe.drop(bad_parents, axis = 0, inplace = True)
    dataframe=dataframe.reset_index(drop = True)
    prr = list(dataframe['parents '])
    bad_parents = get_badParents(prr)
    if len(bad_parents) == 0:
        break


# Sorting the entire dataframe wrt 'fee' column
final_df=dataframe.sort_values(by = ['fee'], ascending = False, ignore_index = True)


# Here we maximize the weight
# The function returns a list of transaction ids which maximize the 'fee' for the weight 4 mil
def result(df):
    li_txids = []
    wg = 0
    for i in range(df.shape[0]):
        wg += df.iloc[i,2]
        if wg <= 4000000:
            li_txids.append(df.iloc[i,0])
        else:
            wg -= df.iloc[i,2]
        if wg >= 4000000:
            break
    return li_txids


result_ls = result(final_df) # here we get our results , i.e the transaction ids required

# This will give you the 'block_file' with all the transaction ids
textfile = open("block_file.txt", "w")
for element in result_ls:
    textfile.write(element + "\n")
textfile.close()

print("Output is in the file \"block_file.txt\"")









