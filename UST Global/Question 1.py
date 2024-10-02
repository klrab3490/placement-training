n = int(input("Enter a number: "))
m = (2*n)-1
for i in range(m):
    for j in range(m):
        print(max(abs(i-m//2), abs(j-m//2))+1, end=" ")
    print()

