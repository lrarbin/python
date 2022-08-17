# 15/05/2021
# Laurence Arbin
# Looping through a slice


# Looping through a slice with a for loop


names = ['tom', 'dick', 'harry', 'velma']

print("Here are are the names of the last 3 registrations.")

for name in names[-3:]:
    print(name.title())