x = "GAGCCTACTAACGGGAT"
y = "CATCGTAATGACGGCCT"
c = 0
for i in range(len(x)):
    if x[i] != y[i]:
         c += 1
print(c)