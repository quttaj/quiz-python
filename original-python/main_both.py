from question_model import Question
from quiz_data import question_data
from quiz_brain_both import QuizBrain
from quiz_ui_both import QuizInterface, SettingsWindow
from random import shuffle
import html

question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)
settings = SettingsWindow()
quiz = QuizBrain(question_bank, settings.number_of_players, settings.current_team)

quiz_ui = QuizInterface(quiz)
QuizBrain.save_results_to_file(quiz)

#print("You've completed the quiz")
#print(f"Your final score was: {quiz.score}/{quiz.question_no}")