from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questions = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)

while quiz.still_has_question():
    quiz.next_question()

print(f"Quiz completed.\nYour final score was: {quiz.score}/{len(questions)}")