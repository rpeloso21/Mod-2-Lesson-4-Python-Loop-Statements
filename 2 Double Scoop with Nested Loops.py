# Task 1

import random

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
times = ("morning", "afternoon", "evening")
moods = ["happy", "sad", "angry", "anxious", "energetic"]


for day in days_of_the_week:
    for time in times:
        mood = random.choice(moods)
        print(f"It is currently {day} {time}, and I am feeling very {mood}.")
