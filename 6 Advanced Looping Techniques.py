# Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres[1:4]:
    print(f"Our sublist includes {genre}.")

# Task 2

new_list = [genre + " Music" for genre in genres]

print(new_list)

# Task 3
counter = 10
for i in range(1, counter+1):
    print(f"The beat drops in {counter}!")
    counter -= 1

print("The beat drops now!!!")