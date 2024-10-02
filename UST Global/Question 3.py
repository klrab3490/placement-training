n = int(input("Enter a number: "))
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        if i % 2 == 0:            
            if j < n - 1:
                row.append(i + 1)
            else:
                row.append(i + 2)
        else:
            if j == 0:
                row.append(i + 2)
            else:
                row.append(i + 1)
    matrix.append(row)

print("")
print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))
