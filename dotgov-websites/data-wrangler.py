import csv

with open("censys-federal-snapshot.csv", "rb") as infile, open("censys-federal-snapshot-cleaned.csv", "wb") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = set('_"/.$')
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)