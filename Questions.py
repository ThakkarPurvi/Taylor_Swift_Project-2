

class Questions:
    def __init__(self, questions, options):
        self.questions = questions
        self.options = options

    def display_question_1(self):
        print(self.questions[0])
        
    def disply_option_1(self):
        print("\nChose from:\n")
        print(self.options[0])
        
    def get_question_1(self):
        return self.questions[0]
    
    def get_option_1(self):
        print("\nChose from:\n")
        return self.options[0]
    
    def get_number_of_questions(self):
        return len(self.questions)
    
    def get_number_of_options(self):
        return len(self.options)