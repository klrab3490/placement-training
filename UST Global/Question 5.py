# Diagonal Matrix Generation
# This program generates a square matrix of size n x n based on specific diagonal patterns.
# The user is prompted to enter a number n, and the matrix is populated as follows:
# - The main diagonal (top-left to bottom-right) contains the value of the row index (i).
# - The anti-diagonal (top-right to bottom-left) contains the value of the column index (j).
# - All other positions in the matrix are filled with spaces for proper alignment.
# The resulting matrix is printed in a formatted manner.


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

    