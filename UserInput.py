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
        return self.answer

    def ask_answer(self, index):
        number_of_options = len(options_taylor[index])
        user_answer = input("Option number: ")
        if user_answer not in range(1, number_of_options + 1):
            option = options_selection[index]
            answer = option[user_answer]
            self.answer[index + 1] = answer
        else:
            print("Not in the range of answer available")
            self.get_answer(self, index)
            
    def get_vibe(self):
        index_question = 3
        answer = self.handle_user_answer(index_question)
        return answer

    def get_subject(self):
        index_first_question = 1
        answer_1 = self.handle_user_answer(index_first_question)
        if answer_1 == "ME":
            return answer_1
        elif answer_1 == "OTHER":
            index_second_question = 2
            answer_2 = self.handle_user_answer(index_second_question)
            return answer_2

    def get_type_playlist(self):
        index_first_question = 0
        answer = self.handle_user_answer(index_first_question)
        return answer

    def handle_user_answer(self, index_question):
        self.display_question(index_question)
        self.ask_answer(index_question)
        return self.get_answer()[index_question+1]