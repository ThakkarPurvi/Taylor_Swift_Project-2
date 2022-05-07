from TaylorQuestions import TaylorQuestions
from Taylor_questions_stored import options_taylor, options_selection

class UserInput:
    def __init__(self, question):
        self.question = question
        self.answer = {}

    def display_question(self, index):
        self.question.display_question(index)
        self.question.display_option(index)
        
    def get_answer(self):
        print("ans: ", self.answer)
        return self.answer

    def ask_answer(self, index):
        number_of_options = len(options_taylor[index])
        user_answer = input("Option number: ")
        if user_answer not in range(1, number_of_options + 1):
            option = options_selection[index]
            answer = option[user_answer]
            self.answer[index + 1] = answer
            print("here ", answer)
        else:
            print("Not in the range of answer available")
            self.get_answer(self, index)
    
