from DatabaseManager import DatabaseManager
from UserInput import UserInput
from TaylorQuestions import TaylorQuestions
from Taylor_questions_stored import options_taylor, options_selection


class Factory:
    def __init__(self, user_input, database_manager):
        self.user_input = user_input
        self.database_manager = database_manager
        self.nb_songs = 5
        
    def handle_question(self):
        answer = self.user_input.get_type_playlist()
        if answer == "1":
            self.database_manager.create_random_playlist(self.nb_songs)
        elif answer == "2":
            subject = self.user_input.get_subject()
            vibe = self.user_input.get_vibe()
            self.database_manager.create_personalized_playlist(vibe, subject, self.nb_songs)
        else:
            print(answer)
