import time

def msort3(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

allNames = names_1 + names_2
sortedName = msort3(allNames)

duplicate2 = []
for i in range(len(sortedName)-1) :
    if sortedName[i] == sortedName[i+1]:
        duplicate2.append(sortedName[i])


end_time = time.time()
print (f"{len(duplicate2)} duplicates:\n\n{', '.join(duplicate2)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
