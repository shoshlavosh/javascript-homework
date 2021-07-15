def reorganize_produce_summary(day, summary):
    """Takes in a day's produce summaries and returns a /n
    more organized output"""

    print(f"Day {day}")
    #loop over each line in the summary
    for item in summary:

        the_file = open(summary)
        #opens the file of summaries for Day 1
        for line in the_file: 
        #loops over each line in the file
            line = line.rstrip() 
            #removes blank spaces in lines, saves to variable "line"

            words = line.split('|')
            #adds a "|" between each word and saves to variable "words"

            melon = words[0]
            #assigns variable "melon" to index 0 (first item) of "words"
            count = words[1]
            #assigns variable "count" to index 1 (second item) of "words"
            amount = words[2]
            #assigns variable "amount" to index 2 (third item) of "words"
            

        print()
        print(f"Delivered {count} {melon}s for total of ${amount}")
        #f-string that prints out melon, count, and amount data for each line
    

        the_file.close()
        print()


reorganize_produce_summary("1", "um-deliveries-20140519.txt")
reorganize_produce_summary("2", "um-deliveries-20140520.txt")
reorganize_produce_summary("3", "um-deliveries-20140521.txt")    

#solution:
# def melon_count(day_number, path):
#     """Given day number & path to the deliveries, produce report.

#     Opens the deliveries file at [path], processes each line,
#     and generates report in all uppercase.
#     """

#     print("Day", day_number)
#     delivery_log = open(path)

#     for line in delivery_log:
#         line = line.rstrip()
#         words = line.split('|')

#         melon = words[0]
#         count = words[1]
#         amount = words[2]

#         # or you could do this with "list unpacking":
#         #
#         # melon, count, amount = words
        
#         print("Delivered {} {}s for total of ${}".format(
#             count, melon, amount))

#     delivery_log.close()


# melon_count(1, "um-deliveries-20140519.txt")
# melon_count(2, "um-deliveries-20140520.txt")
# melon_count(3, "um-deliveries-20140521.txt")

#original code from assignment:
# print("Day 1")
# #prints a line to explain that this is for Day 1
# the_file = open("um-deliveries-20140519.txt")
# #opens the file of summaries for Day 1
# for line in the_file: 
# #loops over each line in the file
#     line = line.rstrip() 
#     #removes blank spaces in lines, saves to variable "line"

#     words = line.split('|')
#     #adds a "|" between each word and saves to variable "words"

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
#     #f-string that prints out data for each line
# the_file.close()
# #closes the file


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
