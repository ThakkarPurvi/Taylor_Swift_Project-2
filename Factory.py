from DatabaseManager import DatabaseManager
from UserInput import UserInput
from TaylorQuestions import TaylorQuestions
from Taylor_questions_stored import options_taylor, options_selection


class Factory:
    def __init__(self, user_input, database_manager, options):
        self.user_input = user_input
        self.database_manager = database_manager
        self.options = options
        self.nb_songs = 5

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
            print(answer_2)
            return answer_2

    def get_type_playlist(self):
        index_first_question = 0
        answer = self.handle_user_answer(index_first_question)
        return answer

    def handle_user_answer(self, index_question):
        self.user_input.display_question(index_question)
        self.user_input.ask_answer(index_question)
        return self.user_input.get_answer()[index_question+1]
        
    def handle_question(self):
        answer = self.get_type_playlist()
        if answer == "1":
            a = self.database_manager.create_random_playlist(self.nb_songs)
            print(a)
        elif answer == "2":
            subject = self.get_subject()
            vibe = self.get_vibe()
            print(subject, vibe)
            b = self.database_manager.create_personalized_playlist(vibe, subject, self.nb_songs)
            print(b)
        else:
            print(answer)

        