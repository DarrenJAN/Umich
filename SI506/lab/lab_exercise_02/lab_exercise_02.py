# Lab Exercise 02
print('Lab Exercise 02 \n')

# Setup
shows = [
    "Action Pack, Kids, 1, exciting",
    "The Queen of Flow, Telenovela, 2, Emotional",
    "Hype House, Reality, 1, scandalous",
    "Queer Eye, Lifestyle, 6, Feel-good",
    "Cocomelon, Kids, 4, educational",
    "Emily in Paris, Romantic Comedy, 2, Quirky",
    "The Witcher, Fantasy, 2, Exciting",
    "Stay Close, Crime, 8, emotional",
    "Cobra Kai, Dramedy, 4, exciting",
    "Cheer, Reality, 2, exciting"
]

# Problem 01 (3 points)

genres = []
for element in shows:
    e_split = element.split(', ')
    genre = e_split[1]
    genres.append(genre)

print(f"\n1. genres = {genres}")

# Problem 02 (4 points)

emotional_shows = []
for element in shows:
    e_split = element.split(', ')
    if 'emotional' == e_split[3].lower():
        emotional_shows.append(e_split[0])

print(f"\n2. emotional_shows = {emotional_shows}")

# Problem 03 (4 points)

count = 0
for element in shows:
    e_split = element.split(', ')[0]
    title = e_split.split()
    if len(title) > 1:
        count = count + 1

print(f"\n3. There are a total of {count} shows with more than one word in their title.")

# PROBLEM 4 (4 Points)
new_shows = []
for element in shows:
    e_split = element.split(', ')[2]
    if int(e_split) < 3:
        new_shows.append(element.split(', ')[0])

# print(f"\n4. {new_shows}")

# PROBLEM 5 (5 Points)
num = 0
longest_show = None
for element in shows:
    e_split = element.split(', ')
    if int(e_split[2]) > num:
        num = int(e_split[2])
        longest_show = e_split[0]

# print(f"\n5. {longest_show}")



# END LAB EXERCISE
