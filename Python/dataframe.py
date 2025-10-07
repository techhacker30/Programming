import pandas as pd

#DataFrame != A tabular data structure with row and columns. (2 Dimensional)#		  Similar to an excel spreadsheet

data = {"Name": ["harry", "patrick", "Nobeljoh"],
	"Age": [43, 23, 32]
}

#DataFrame is a Contacture , index help to change the index
dataframe = pd.DataFrame(data, index=["Employee 1", "Employee2", "Employee 3"])

print(dataframe)

#.loc[] is used to access the element using a key
print(dataframe.loc["Employee 1"])
#not allowed
#print(dataframe.loc["patrick"])

#use .iloc[] to access element using int no like arry 0-n
print(dataframe.iloc[2])

#add a new column 
dataframe["job"] = ["Cook", "N/A", "Cashier"]

print(f"\n{dataframe}")

#add a new row

new_row = pd.DataFrame([{"Name": "Sandy", "Age":28, "job": "Engineer"}], index=["Emloyee 4"])
dataframe = pd.concat([dataframe, new_row])

print(dataframe)
