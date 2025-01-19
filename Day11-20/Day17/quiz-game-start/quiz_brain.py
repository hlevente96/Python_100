class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        ans = input(f"Q.{self.q_number} {question.text} (True/False): ")
        self.check(ans, question.answer)

    def still_has_question(self):
        return self.q_number == len(self.q_list)

    def check(self, ans, real):
        if ans.lower() == real.lower():
            self.score += 1
            print("GOOD")
        else:
            print("BAD")
        print(f"Your score is: {self.score}/{self.q_number}")