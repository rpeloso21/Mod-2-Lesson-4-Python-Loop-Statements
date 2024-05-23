# Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

counter = 1

for genre in genres:

    print(f"I am now listening to track number {counter}.  The genre is {genre}.")
    counter += 1

# Task 2

counter = 1

while True:
    for genre in genres:
        print(f"I am now listening to track number {counter}.  The genre is {genre}.")
        counter += 1

    if genre == "Classical":
        break

    # Task 3

not_suitable = ["Jazz", "Classical"]
counter = 1

for x in range(len(genres)):
    genre = genres[x]
    if genre in not_suitable:
        pass
    else:
        print(f"The light show is now ready for track number {counter}.  We will be listeing to some {genre}.")
        counter += 1
