from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager
from Questions import Questions
from TaylorQuestions import TaylorQuestions
from Taylor_questions_stored import questions_taylor, options_taylor, options_selection
from UserInput import UserInput
from Factory import Factory


"""
Create an automated tailored Taylor Swift playlist.

"""

def main():
    database_name = "taylor_swift_project"
    table_name = "master_song_list"
    database = DatabaseConnection(database_name)
    connection = database.create_connect()
    database_manager = DatabaseManager(connection)
    is_table_in_db = database_manager.ensure_table_exist(table_name)
    if is_table_in_db is True:
        taylor_questions = TaylorQuestions(questions_taylor, options_taylor)
        user = UserInput(taylor_questions)
        factory = Factory(user, database_manager)
        songs = factory.handle_question()
        print(songs)
    connection.close()

if __name__ == "__main__":
    main()