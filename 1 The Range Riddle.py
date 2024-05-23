import random

moods = ["happy", "sad", "angry", "anxious", "energetic"]

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for x in range(0, 7):   # Using the range funcion seems like an unnecessary step, but I am trying to follow the instructions.
                        # Normally, I would just use... for day in days_of_the_week.
    day = days_of_the_week[x]
    mood = random.choice(moods)
    print(f"Today is {day}. I wake up feeling quite {mood}, and I know it will be that kind of day.")
