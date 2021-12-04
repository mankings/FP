def allTeams():
    teams = []
    print("Stage 1 - Team Input. Leave empty to end.")
    while True:
        team = input("Enter team name: ")
        if (team == ""): 
            print()
            break
        teams.append(team)
    return teams

def allMatches(teams):
    matchList = []
    for home in range(len(teams)):
        for away in range(len(teams)):
            if home != away:
                matchList.append((teams[home], teams[away]))
    return(matchList)

def setResults(matches):
    results = {}
    for match in matches:
        print(match[0] + " vs " + match[1])
        result = (int(input(match[0] + " score: ")), int(input(match[1] + " score: ")))
        results[match] = result
        print()

    return results

def scoreTable(teams, results):
    table = {}

    for team in teams:
        wins = 0
        ties = 0
        losses = 0
        marcados = 0
        sofridos = 0
        points = 0

        for match, result in results.items():
            if(team == match[0]):
                if(result[0] > result[1]):
                    wins += 1
                elif(result[0] < result[1]):
                    losses += 1

                marcados += result[0]
                sofridos += result[1]
                
            elif(team == match[1]):
                if(result[0] < result[1]):
                    wins += 1
                elif(result[0] > result[1]):
                    losses += 1

                marcados += result[1]
                sofridos += result[0]

            if((team == match[0] or team == match[1]) and result[0] == result[1]):
                ties += 1

            points = wins*3 + ties

            table[team] = (wins, ties, losses, marcados, sofridos, points)
    
    return table

def printTable(table):
    sortedTable = sorted(table.keys(), key=lambda t: table[t][5], reverse=True)
    print("{:6} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("Equipa", "Vit", "Emp", "Der", "Mar", "Sof", "Pon"))
    print()
    for team in sortedTable:
        print("{:>6} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(team, table[team][0], table[team][1], table[team][2], table[team][3], table[team][4], table[team][5]))

def main():
    teamList = allTeams()
    matchesList = allMatches(teamList)
    resultsList = setResults(matchesList)
    finalTable = scoreTable(teamList, resultsList)
    printTable(finalTable)

main()