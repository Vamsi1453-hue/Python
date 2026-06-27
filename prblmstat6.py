#cricket scores avg
n = int(input("Enter number of teams: "))
teams = []
scores = []

for _ in range(n):
    name, run = input("Enter team name and score (e.g. India 250): ").split()
    run = int(run)
    teams.append((name, run))
    scores.append(run)

highest_team = max(teams, key=lambda x: x[1])[0]
average_score = sum(scores) / n
above_avg_teams = [name for name, run in teams if run > average_score]

print("Highest :", highest_team)
print("Average :", round(average_score, 1))
print("Above Average")
for team in above_avg_teams:
    print(team)

