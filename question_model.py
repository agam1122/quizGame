from data import question_data


class Question:

    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer


question_bank = []
for i in range(0, 12):
    question_text = f"{question_data[i]["text"]}"
    question_answer = f"{question_data[i]["answer"]}"
    quiz = Question(question_text, question_answer)
    question_bank.append(quiz)


