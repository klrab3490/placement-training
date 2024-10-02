# Chair Arrangement Validation
# This program checks the arrangement of chairs labeled from A to Z based on their ordinal positions in the English alphabet.
# It prompts the user to enter a string, which represents the arrangement of chairs.
# The program compares each character in the input string (converted to lowercase) with the corresponding 
# letter in the alphabet (a to z) to determine how many chairs are correctly placed.
# It then outputs the count of correctly placed chairs.


print("Chair Arrangement Validation")
s = input("Enter The String: ") # Get the input string which may contain chapital letters
s.lower() # Convert to lowercase
n = len(s) # Get the length of the string
letters = "abcdefghijklmnopqrstuvwxyz" 
count = 0

for i in range(n):
    if s[i] == letters[i]:
        count += 1

print(count)