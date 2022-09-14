# Author: Tanner Bacon
"""
Write a program that prompts the user to enter in the number 
of teams and then, for each team, the number of games played. 
For each game played, for each team, you will enter the team's 
score and the opponent's score. You will then determine if the 
current team won the game and add that to the wins. If not, 
add that to the losses. Once that team's games have been entered, 
you will calculate the win/loss percentage by using the formula: 
wins / total number of games. Then display the team name that 
had the highest win/loss percentage along with their percentage.
"""

# Collect Input
iNumTeams = int( input("Enter the number of teams: "))
sHighTeam = ""
fHighTeam = 0.0

# Repeat for each team
for iTeamCount in range(1, (iNumTeams + 1)):
    # Get the team name and games played
    sTeamName = input("\nEnter the team name: ")
    iNumGames = int( input("Enter the number of games " + sTeamName + " played: "))

    # Reset games for each team
    iWinCount = 0
    iLoseCount = 0

    for iGames in range(1, (iNumGames + 1)):
        # Get the game scores
        iTeamScore = int( input("Enter the score for " + sTeamName + ": "))
        iOppScore = int( input("Enter the oponent's score: "))

        # Ensure that the user is not inputting a tie
        while (iTeamScore == iOppScore):
            print("You cannot have a tie")
            iTeamScore = int( input("Enter the score for " + sTeamName + ": "))
            iOppScore = int( input("Enter the oponent's score: "))

        # Check for win or loss and add to record
        bWin = iTeamScore > iOppScore
        if bWin: iWinCount += 1
        else: iLoseCount += 1
    
    # Calculate win percentage
    fWinPercentage = iWinCount / iNumGames

    # Compare current and highest win percentage
    if (fWinPercentage > fHighTeam):
        fHighTeam = fWinPercentage
        sHighTeam = sTeamName

# Display team with highest percentage and their percentage
print(sHighTeam + " had the highest win percentage with " + str(fHighTeam))