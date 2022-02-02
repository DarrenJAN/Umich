# START PROBLEM SET 2
print("Problem Set 1\n")

# PROBLEM 1 (10 points)
print("Problem 1\n")
top_shows = ["Only Murders in the Building | Steve Martin | comedy | 93 | 2021",
"Reservation Dogs | D'Pharaoh Woon-a-Tai | Crime | 88 | 2021",
"Justified | Timothy Olyphant | crime | 95 | 2010",
"What We Do in the Shadows | Matt Berry | horror | 92 | 2019",
"Better Things | Pamela Adlon | Comedy | 84 | 2016"]

stars = []

for show in top_shows:
    stars.append(show.split(" | ")[1])
print(f"stars list = {stars}\n") # UNCOMMENT TO CHECK


# PROBLEM 2 (12 points)
print("Problem 2\n")
comedies = []

for show in top_shows:
    if("Comedy" in show or "comedy" in show):
        comedies.append(show.split(" | ")[0])

print(f"comedies list = {comedies}\n") # UNCOMMENT TO CHECK


# PROBLEM 3 (10 points)
print("Problem 3\n")
total_ratings = 0
for show in top_shows:
    total_ratings += int(show.split(" | ")[3])
avg_rating  = total_ratings / 5

print(f"avg_rating is = {avg_rating}\n")

# PROBLEM 4 (12 points)
print("Problem 4\n")
above_avg = []
below_avg = []

for show in top_shows:
    if int(show.split(" | ")[3]) > avg_rating:
        above_avg.append(show.split(" | ")[0])
    if int(show.split(" | ")[3]) < avg_rating:
        below_avg.append(show.split(" | ")[0])

print(f"above average shows = {above_avg}\n") # UNCOMMENT TO CHECK
print(f"below average shows = {below_avg}\n") # UNCOMMENT TO CHECK


# PROBLEM 5 (18 points)
print("Problem 5\n")

top_shows_new = []
for show in top_shows:
    rate = round(float(show.split(" | ")[3]) / 20, 1)
    top_shows_new.append(f"{show} | {rate}");

print(f"top_shows_new = {top_shows_new}\n") # UNCOMMENT TO CHECK

# PROBLEM 6 (15 points)
print("Problem 6\n")
min_year = 9000
oldest_show = []
for element in top_shows:
    show = element.split(' | ')
    year = int(show[-1])
    if year < min_year:
        min_year = year
        oldest_show = show[0]

print(f"min_year = {min_year}\n") # UNCOMMENT TO CHECK
print(f"oldest_show = {oldest_show}\n") # UNCOMMENT TO CHECK
# Problem 7 (10 points)
print("Problem 7\n")
content = ["Parasite: Film",
    "The Biggest Little Farm: film",
    "Akira: filM",
    "Atlanta: ShOw",
    "Minding the Gap: Film",
    "McCartney 3,2,1: show",
    "Summer of Soul: FiLm",
    "Love, Victor: shOw",
    "The Mole Agent: FILM",
    "It's Always Sunny in Philadelphia: Show",
    "The Great: SHOW"]

select_content = []
for i in range(0, len(content), 2):
    select_content.append(content[i])

print(f"select_content = {select_content}\n") # UNCOMMENT TO CHECK


# PROBLEM 8 (13 points)
print("Problem 8\n")

films = []
shows = []

for show in content:
    if("film" in show.lower()):
        films.append(show.split(":")[0])
    else:
        shows.append(show.split(":")[0])

print(f"films = {films}\n") # UNCOMMENT TO CHECK
print(f"shows = {shows}\n") # UNCOMMENT TO CHECK

# END PROBLEM SET 2