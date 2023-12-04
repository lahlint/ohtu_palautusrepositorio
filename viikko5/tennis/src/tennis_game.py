class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        score = ""

        if self.score1 == self.score2:
            score = self.get_score_tie()
        elif self.score1 >= 4 or self.score2 >= 4:
            score = self.get_score_advantage_or_win()
        else:
            score = self.get_score_no_winner()

        return score
    
    def get_score_tie(self):
        scores = ["Love-All","Fifteen-All","Thirty-All"]
        if self.score1 <= 2:
            score = scores[self.score1]
        else:
            score = "Deuce"
        return score
    
    def get_score_advantage_or_win(self):
        minus_result = self.score1 - self. score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def get_score_no_winner(self):
        score = ""
        temp_score = 0
        scores = ["Love","Fifteen","Thirty","Forty"]
        for i in range(1, 3):
            if i == 1:
                temp_score = self.score1
            else:
                score = score + "-"
                temp_score = self.score2
            score = score + scores[temp_score]
        return score

