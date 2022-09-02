from turtle import Turtle

#setting constants
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    
    def high_score_update(self):

        line_ = list()
        high_score = 0

        # writing high score to file for persistency
        with open("score.txt", "r") as fopen:

            for line in fopen:
                line_ = line.split(":")
            if len(line_) == 0:
                high_score = 0
            else:
                high_score = int(line_[1].strip())
        
        self.goto(0, 50)
        self.write(f"High Score: {high_score}", align="center", font=("courier", 20, "normal"))


    def update_scoreboard(self):

        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 24, "normal"))
        self.save_high_score()
        self.high_score_update()
        
    def save_high_score(self):

        score_list = list()

        with open("score.txt", "r") as fopen:

            for line in fopen:
                score_list = line.split(":")
        with open("score.txt", "w") as fwrite:
            
            if len(score_list) == 0:
                fwrite.write(f"Score: {self.score}")
            else:
                if int(score_list[1].strip()) < self.score:
                    fwrite.write(f"Score: {self.score}")
                else:
                    fwrite.write(f"Score: {int(score_list[1].strip())}")
                    








