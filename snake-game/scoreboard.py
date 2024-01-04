class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(0, 270)
        self.pendown()
        self.color("white")
        self.hideturtle()
        self.score = 0
        with open("data.txt", mode="r") as highscore:
            self.highscore= int(highscore.read())
        self.score_counter()

    def score_counter(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as highscore:
                highscore.write(f"{self.highscore}")
        self.score = 0
        self.score_counter()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=FONT, align=ALIGNMENT)
    def increase_score(self):
        self.score += 1