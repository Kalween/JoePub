from question_model import Question
from data import question_data


questions = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["questions"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)