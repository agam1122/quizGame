from question_model import question_bank

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        c = 0
        t = 0
        q = 0
        for question in question_bank:
            q += 1
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_input = input(f"Q.{self.question_number}: {current_question.question} (True/False): ").lower()
            if user_input == current_question.answer.lower():
                print("Correct Answer\n")
                c += 1
                t += 1
                if q == 12:
                    print("You have completed the quiz.")
                    print(f"Your final score is {c}/{t}")
                    break
                print(f"Your score is {c}/{t}\n")
            else:
                t += 1
                print("Wrong Answer\n")
                if q == 12:
                    print("You have completed the quiz.")
                    print(f"Your final score is {c}/{t}")
                    break
                print(f"Your score is {c}/{t}\n")

