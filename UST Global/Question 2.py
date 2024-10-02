s = input("Enter The String: ")
n = len(s)
letters = "abcdefghijklmnopqrstuvwxyz"
s.lower()
count = 0

for i in range(n):
    if s[i] == letters[i]:
        count += 1

print(count)