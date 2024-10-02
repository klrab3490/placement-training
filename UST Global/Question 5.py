



n = int(input("Enter a number: "))
matrix = []

for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if i == j:
            row.append(i)
        elif i + j == n + 1:
            row.append(j)
        else:
            row.append(" ")  # Keep space for alignment

    matrix.append(row)

print("\nMatrix: ")
# Printing the matrix with formatted output
for row in matrix:
    print(" ".join(str(x) if x != " " else " " for x in row))

    