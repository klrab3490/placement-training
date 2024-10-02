# Matrix Pattern Generation
# This program generates a (2n-1) x (2n-1) matrix based on a specific pattern defined by the input number n.
# The center of the matrix contains the value 1, and as you move towards the edges, the values increase
# incrementally, with the border cells containing the value n.
# The program uses absolute differences from the center to determine the values for each position in the matrix.

print("Matrix Pattern Generation")
n = int(input("Enter a number: "))
m = (2*n)-1
for i in range(m):
    for j in range(m):
        print(max(abs(i-m//2), abs(j-m//2))+1, end=" ")
    print()

