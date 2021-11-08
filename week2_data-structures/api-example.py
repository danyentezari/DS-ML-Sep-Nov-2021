# 1 - Use cURL to download file from cloud
# curl -o sample_sales.csv -H "Accept: application/csv" -X GET https://storage.googleapis.com/example-for-astrolabs/sample_sales.csv

# 2 - Import 'csv' library
import csv

# 3 - Open the 'sample-sales.csv' file
csvFile = open('./sample_sales.csv')

# 4 - Read the file into a List
csvList = list(csv.reader(csvFile))

# 5 - List operations
# print( csvList[1][13] )

# 6 - Slice Notation
# list[startIndex:endIndex]
# list[startIndex:endIndex:stride]


# Skipping every other element
# prices = [100,200,300,400,500,600]
# print( prices[1::2] )


sales = [
    10000,
    500,
    750,
    8000,
    250,
    5500,
    5000
]

newSales = []
for value in sales:
    if value > 100 and value < 800:
        newSales.append(value)
print( newSales )


newSales2 = [ value for value in sales if value > 100 and value < 800 ]
print(newSales2)
