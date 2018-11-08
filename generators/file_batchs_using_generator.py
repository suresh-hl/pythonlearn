import csv

file = open('/Users/sureshh/bigdata/FL_insurance_sample.csv', 'r')
csv_read = csv.DictReader(file, delimiter=',')

lines = (line['point_granularity'] for line in csv_read)

batch = 1000

batchlines = []
batchnum = 0

while True:
    try:
        for i in range(1, batch + 1):
            batchlines.append(next(lines))
            #add logic here
        print(len(batchlines))
        batchlines = []
        batchnum += 1
    except StopIteration:
        print(len(batchlines))
        print(batchnum + 1)
        print('Reached EOF')
        file.close()
        break
    except:
        print("Unknown exception")
        file.close()
        break
