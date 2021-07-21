# """Generate sales report showing total melons each salesperson sold."""

# #create two empty lists, one for salespeople, one for the # of melons sold
# #suggestion = better variable names. "names_list", "num_sold"
# salespeople = []
# melons_sold = []

# #this opens the file and assigns it to variable, "f"
# #suggestion = name this something more descriptive than a single letter
# f = open('sales-report.txt')

# #loops through each line of the file "f"
# for line in f:
#     #removes whitespace on each line
#     line = line.rstrip()
#     #splits each piece of data on the line at the pipe symbol 
#     # and assigns it to "entries"
#     entries = line.split('|')

#     #assigns salesperson to index 0 of entries
#     #suggestion = use better variable, like "name"
#     salesperson = entries[0]
#     #assigns the number of melons sold to index2 of entries 
#     # and changes that to an integer
#     melons = int(entries[2])

#     #checks to see if data at entries[0] is already in salespeople list
#     if salesperson in salespeople:
#         #if yes, assign to variable "position"
#         #
#         position = salespeople.index(salesperson)

#         #melons_sold[position] = melons_sold + melons
#         melons_sold[position] += melons

#     else:
#         #otherwise, add salesperson to list
#         salespeople.append(salesperson)
#         #add melons to list
#         melons_sold.append(melons)


# #loop over each index spanning the length of the list of salespeople
# for i in range(len(salespeople)):
#     #print how many melons each person sold (data pulled from the lists)
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# #suggestion: close the file
# f.close()

#REDO THIS MESS
file = open('sales-report.txt')

#loops through each line of the file "f"
for line in file:
    #removes whitespace on each line
    line = line.rstrip()
    #splits each piece of data on the line at the pipe symbol 
    # and assigns it to "entries"
    entries = line.split('|')

    #create variables for salesperson name & melon qty sold
    #at the respective indices for entries
    name = entries[0]
    melon_qty = entries[2]

    #create empty dictionary
    sales_info = {}

    #populate dictionary with salesperson and qty of melons sold
    sales_info[name] = melon_qty

    # print(sales_info)

    # to print all info
    for name, melon_qty in sales_info.items():
        print(f"{name} sold {melon_qty} melons.")


#close the file
file.close()