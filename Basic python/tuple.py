name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict = {}
for line in handle:
    if not line.startswith("From ") :
        continue
    list = line.split()
    hour = list[5].split(":")[0]
    dict[hour] = dict.get(hour,0) + 1

sorted = sorted([ (k,v) for k,v in dict.items()])
for k,v in sorted:
    print(k,v)
