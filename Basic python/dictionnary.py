name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict = {}
for line in handle:
    if not line.startswith("From ") :
        continue
    list = line.split()
    dict[list[1]] = dict.get(list[1],0) + 1

namebiggest = None
biggest = None
for word,value in dict.items():
    if biggest is None or value > biggest:
        namebiggest = word
        biggest = value

print(namebiggest,biggest)
