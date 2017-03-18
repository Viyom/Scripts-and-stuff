import csv
f = open('output.txt', 'w')
with open('throughput.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
	try:
            f.write(str(row['Time']) + " " + str(int(row['Length']))+'\n')
	except:
	    print "Val ::", row

