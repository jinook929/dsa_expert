# Tournament Winner
# There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.

# Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing the name of the team. The results array contains information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array means that the home team in the corresponding competition won and a 0 means that the away team won.

# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.

# Sample Input
competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]
results = [0, 0, 1]
# Sample Output
# "Python"
# // C# beats HTML, Python Beats C#, and Python Beats HTML.
# // HTML - 0 points 
# // C# -  3 points
# // Python -  6 points

def tournament_winner(competitions, results):
  winners = {}
  for i in range(len(competitions)):
    if results[i] == 1:
      team = competitions[i][0]
      winners[team] = 1 if not team in winners else winners[team] + 1
    else:
      team = competitions[i][1]
      winners[team] = 1 if not team in winners else winners[team] + 1
  
  ### using max
  return max(winners, key = winners.get)

  ### using for loop
  # max_wins = 0
  # winner = None
  # for winning_team in winners:
  #   if winners[winning_team] > max_wins:
  #     max_wins = winners[winning_team]
  #     winner = winning_team    
  # return winner

  ### using reduce
  # import functools
  # winner = functools.reduce(lambda acc, team: {team: winners[team]} if winners[team] > list(acc.values())[0] else acc, winners, {"winner": 0})
  # return list(winner.keys())[0]

def tournament1(competitions, results):
    # competitions: [homeTeam, awayTeam] string (< 30 chars)
    # results: [1] for homeTeam win, [0] for awayTeam win
    winner = ""
    scores = {winner: 0}
    for i in range(len(results)):
        idx = 0 if results[i] == 1 else 1
        team = competitions[i][idx]
        if team not in scores:
            scores[team] = 1
        else:
            scores[team] += 1
        if scores[team] > scores[winner]:
            winner = team
    return winner

def tournament2(competitions, results):
    scores = {"highest": 0, "winner": ""}
    for i in range(len(results)):
        idx = 0 if results[i] == 1 else 1
        team = competitions[i][idx]
        scores[team] = 1 if team not in scores else scores[team] + 1
        if scores[team] > scores["highest"]:
            scores["highest"] = scores[team]
            scores["winner"] = team
    return scores["winner"]

# for _ in range(9999999):
#   tournament_winner(competitions, results)
print(tournament_winner(competitions, results))

# for _ in range(9999999):
#   tournament1(competitions, results)
# print(tournament1(competitions, results))
# for _ in range(9999999):
#   tournament2(competitions, results)
# print(tournament2(competitions, results))