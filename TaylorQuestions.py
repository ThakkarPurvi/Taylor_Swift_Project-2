from Questions import Questions


class TaylorQuestions(Questions):
    def __init__(self, question, option):
        super().__init__(question, option)
        self.option_number = "Option number: "
        self.chose_from = "\nChose from:\n"
        
    def display_question(self, index):
        print(self.questions[index])
        
    def display_option(self, index):
        qlist = (self.options[index].keys())
        print(self.chose_from)
        for i in qlist:
            print(i + "\n")

    def get_question(self, index):
        return self.questions[index]
    
    def get_option(self, index):
            return self.options[index]
    
    def get_number_of_questions(self):
        return len(self.questions)
    
    def get_number_of_options(self):
        return len(self.options)
    