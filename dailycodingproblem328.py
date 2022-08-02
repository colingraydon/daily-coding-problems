#A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent game, the loser transfers some points to the winner, 
# where the amount of points transferred depends on how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.
#Implement this system.


#Took this from the international chess foundation's site, FIDE, for calculating K. There are different algorithms used by other organizations
# K is the development coefficient.
# K = 40 for a player new to the rating list until he has completed events with at least 30 games
# K = 20 as long as a player's rating remains under 2400.
# K = 10 once a player's published rating has reached 2400 and remains at that level subsequently, even if the rating drops below 2400.
# K = 40 for all players until their 18th birthday, as long as their rating remains under 2300.
#Also, simple research showed that in a match with 2 players with different k values, they each gain or lose elo according to their own k value
from sympy import true


class ChessElo:

    def init(self, rating, games_played, age, has_reached_2400):

        self.rating = rating
        self.games_played = games_played
        self.age = age
        self.has_reached_2400 = has_reached_2400

    def reaching2400(self):

        if (self.rating > 2399):
            self.has_reached_2400 = true

    #my understanding, from reading the algorithm online, is that this is in the correct priority. 
    def find_k(self):

        if (self.has_reached_2400):
            k = 10
        elif (self.age < 18 and self.rating < 2300 or self.games_played < 30):
            k = 40
        else:
            k = 20

    #for score, 1 represents a p1 victory, .5 is a draw, 0 is a p1 loss
    #this algorithm is the standard one for elo
    def match(p1, p2, score):
        q1 = 10 ** (p1.rating / 400)
        q2 = 10 ** (p2.rating / 400)
        e1 = q1 / (q1 + q2)
        e2 = 1 - e1

        player1_new_rating = p1.rating + p1.find_k() * (score - e1)
        player2_new_rating = p2.rating + p2.find_k() * (score - e2)

        p1.rating = player1_new_rating
        p2.rating = player2_new_rating

        p1.reaching2400()
        p2.reaching2400()

        p1.games_played += 1
        p2.games_played += 1


