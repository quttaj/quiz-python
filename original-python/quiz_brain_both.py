class QuizBrain:
    def __init__(self, questions, number_of_players, team):
        self.question_no = 0
        self.questions = questions
        self.number_of_players = number_of_players
        self.score = 0
        self.score_team = [0, 0]
        self.current_team = team
        self.current_question = None
        self.results_file = "quiz_results.txt"  # Name of the results file

    def has_more_questions(self):
        return self.question_no < len(self.questions)

    def next_question(self):
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        if self.number_of_players == 2:
            self.current_team = 0 if self.current_team == 1 else 1
            return f"Team {self.current_team+1}:\n {q_text}"
        else:
            return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Check the user answer against the correct answer and maintain the score"""

        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            if self.number_of_players == 2:
                self.score_team[self.current_team] += 1
            else:
                self.score += 1
            return True
        else:
            return False

    def get_score(self):
        if self.number_of_players == 2:
            score_percent_team_1 = int(2 * self.score_team[0] / self.question_no * 100)
            score_percent_team_2 = int(2 * self.score_team[1] / self.question_no * 100)
            return (self.score_team[0], self.score_team[1], score_percent_team_1, score_percent_team_2)
        else:
            score_percent = int(self.score / self.question_no * 100)
            return (self.score, score_percent, 0, 0)

    def save_results_to_file(self):
        """Save the quiz results to a text file"""

        with open(self.results_file, "w") as file:
            file.write("Quiz Results\n\n")
            file.write("Number of Players: {}\n".format(self.number_of_players))
            file.write("Team Scores: {}\n".format(self.score_team) if self.number_of_players == 2 else "Score: {}\n".format(self.score))
            file.write("Question Count: {}\n\n".format(self.question_no))

            file.write("Question-wise Results:\n\n")
            for i, question in enumerate(self.questions):
                question_text = question.question_text
                correct_answer = question.correct_answer
                user_answer = ""  # Add logic to get the user's answer for each question if available
                result = "Correct" if user_answer.lower() == correct_answer.lower() else "Incorrect"

                file.write("Question {}: {}\n".format(i + 1, question_text))
                file.write("Correct Answer: {}\n".format(correct_answer))
                file.write("User Answer: {}\n".format(user_answer))
                file.write("Result: {}\n\n".format(result))

            file.write("Final Score: {}\n".format(self.get_score()))

        print("Quiz results have been saved to {}".format(self.results_file))
