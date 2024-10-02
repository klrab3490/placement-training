# Stone Game
# Ladies First
# One Can Take 1 or 4 Stones at once
# 
# 
# Staticstics for 1 to 10
# 1 - Yes = Alice Takes All
# 2 - No = Bob takes the alst one
# 3 - Yes = Alice Takes 1, Bob Takes 1, Alice Takes 1
# 4 - Yes = Alice Takes all 4 stones
# 5 - No = Alice Takes 1, Bob Takes 4
# 6 - Yes = Alice Takes 4, Bob Takes 1, Alice Takes 1
# 7 - Yes = Alice Takes 1, Bob Takes 1, Alice Takes 4, Bob Takes 1
# 8 - Yes = Alice Takes 4, Bob Takes 1, Alice Takes 1, Bob Takes 1, Alice Takes 1
# 9 - No = Alice Takes 4, Bob Takes 1, Alice Takes 1, Bob Takes 1, Alice Takes 1, Bob Takes 1
# 10 - Yes = Alice Takes 1, Bob Takes 4, Alice Takes 1, Bob Takes 1, Alice Takes 1, Bob Takes 1, Alice Takes 1

# So in every 5 Stone Alice wils for  1,3,4 stones while Bob will win for 2,5 stones

print("Stone Game")
n = int(input("Enter a number: "))

if(n%5==0 or n%5==2):
    print("No")
else:
    print("Yes")