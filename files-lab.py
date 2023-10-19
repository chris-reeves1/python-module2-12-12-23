import csv
# created empty lists to store the data. 
companies = []
sales = []

# read data from file
with open('output.csv', newline='') as csvfile:  # r and w are not needed as csv module handles this. 
    reader = csv.reader(csvfile) # reader function from the module, its an iterator which reads all the lines. 
    next(reader) # skip the first line - we dont need the header data. 
    for row in reader: # iterates through each row - each row is represented as a list of strings.
        companies.append(row[0]) #  first index of each list is company name so add to companies list. 
        sales.append([int(x.replace(",", "")) for x in row[1:]]) # iterates from index 1 (first sales data) - changes from str into int, replaces "," with "". finally append to sales list.   

print(sales)
monthly_sum = [sum(x) for x in zip(*sales)] # *sales unpacks the lists in the sales list, into tuples,then sum adds the whole value of tuple giing us a monthyl total.  

yearly_sum = {}
for i in range(len(companies)):
    yearly_sum[companies[i]] = sum(sales[i])

print("Monthly Sales:", monthly_sum)
print("Yearly Sales:")
for company, sales in yearly_sum.items():
    print(company, sales)