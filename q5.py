# ### Problem 5
# Create a SportsTeam Class for tracking sports teams. The class should have the properties team_name_p,
# team_city, and team_ranking_p.
# The class should have a method to change a Team’s ranking. 
# The class should implement the ```__str__``` method so that when an instance of the
# SportsTeam is printed it will output a string containing the team name, team city,
# and team rank (use f strings to format the output).
# Your program should create a SportsTeam instance with an initial ranking of 2.
# Print out the class.
# Your program should change the ranking of the team to 8 using only the class method.
# Print out the class (should use your ```__str__``` method).


# Example Output:
# ```
# The Grizzlies are from Memphis and are 2 in the standings.
# # Update the rating from 2 to 8 from your code
# The Grizzlies are from Memphis and are 8 in the standings.
# ```

class Sports :
    def __init__(self, team_name_p,team_city_p, team_ranking_p):
        self.team_name_p=team_name_p
        self.team_city_p=team_city_p
        self.team_ranking_p=team_ranking_p

       # The has a method to change a Team’s ranking.
    def changeTeamRanking (self,newTeamRanking):
        self.team_ranking_p=newTeamRanking
        return self.team_ranking_p

        # The  ```__str__``` method so that when an instance of the

    def __str__(self):
        return f'{self.team_name_p} is from the city of  {self.team_city_p} with a ranking  {self.team_ranking_p}'

# Your program should create a SportsTeam instance with an initial ranking of 2.

newTeam=Sports("Grizzlies","Memphis",2)

# Print out the class.
print(Sports)
# Your program should change the ranking of the team to 8 using only the class method.
myteamsNewRank=8
Sports.changeTeamRanking(myteamsNewRank)
# Print out the class (should use your ```__str__``` method).
print(Sports)