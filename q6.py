# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role

class ClubMember:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    def __str__(self):
        return f'{self.name}   {self.role}'

# Create ClubMember instances for the following people:
# ```

newMember1 = ("Alfred", "Club President")
newMember2 = ("Troy" , "Club Vice President")
newMember3 = ("Albert" , "Club Secretary")
newMember4 = ("Bob" , "Club Treasurer")


# Added each member instance to a new club_members list that you create.
club_members_list=[newMember1,newMember2,newMember3,newMember4]
# Write the code needed to loop through the club member list and
# print the current number of members in the list, then the member’s name and club role, one per line using f strings.
print(f'The Current Number of Members in the list is {len(club_members_list)}')
for each in club_members_list:
    print(f'{ClubMember.name} {ClubMember.role}' )



# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

