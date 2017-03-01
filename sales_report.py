"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

sales = {}


sales_file = open("sales-report.txt")

for line in sales_file:
    entries = line.rstrip().split("|")
    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in sales:
        sales[salesperson] += melons 
    else:
        sales[salesperson] = melons

sales_file.close()


for salesperson, melon_count in sales.iteritems():
    print "{} sold {} melons".format(salesperson, melon_count)
