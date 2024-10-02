# Matrix Number Generation
# This program generates an n x n matrix based on specific rules for filling in the values.
# For even-indexed rows, the values are generated differently than for odd-indexed rows.
# The last element of each even row is incremented by 1, while the first element of each odd row is also incremented.
# The user is prompted to enter the size of the matrix, and the resulting matrix is displayed.


print("Matrix Number Generation")
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
