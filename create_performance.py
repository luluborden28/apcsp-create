def soccer_games() :
    games = int(input("Enter the number of games played: "))
    return games
games = int(soccer_games())

def soccer_goals() : 
    goals = int(input("Enter the number of goals scored: "))
    return goals

average_goals = soccer_goals() / games

def soccer_assists() :
    assists = int(input("Enter the number of assists made: "))
    return assists

average_assists = soccer_assists() / games

def soccer_saves() :
    saves = int(input("Enter the number of saves made: "))
    return saves

average_saves = soccer_saves() / games


for i in range (0, games, 1) : 

    def soccer_games_min() :
        games = int(input("Enter the number of games played: "))
        return games
    games = int(soccer_games_min())

    def soccer_goals_min() : 
        goals = int(input("Enter the number of goals scored: "))
        return goals

    average_goals = soccer_goals_min() / games

    def soccer_assists_min() :
        assists = int(input("Enter the number of assists made: "))
        return assists

    average_assists = soccer_assists_min() / games

    def soccer_saves_min() :
        saves = int(input("Enter the number of saves made: "))
        return saves

    average_saves = soccer_saves_min() / games

print("Average goals per game: ", average_goals)
print("Average assists per game: ", average_assists)
print("Average saves per game: ", average_saves)