fname = input("Enter file name: ")
fh = open(fname)
somme = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    number = float(line[line.index("0") :])
    somme = somme + number
print("Average spam confidence:",somme/count)
