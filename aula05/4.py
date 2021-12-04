def inputTeamList():
    teamList = []
    while True:
        s = input("Insira uma equipa: ")
        if s == "": break
        teamList.append(s)
    return(teamList)

def allMatches(teams):
    matchList = []
    for home in range(len(teams)):
        for away in range(len(teams)):
            if home != away:
                matchList.append((teams[home], teams[away]))
    return(matchList)

print(allMatches(inputTeamList()))