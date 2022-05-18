from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager


class Model:
    def __init__(self):
        self.database_name = "taylor_swift_project"
        self.table_name = "master_song_list"
        self.database_manager = None
        self.connection = None
        self.nb_songs = 8
        
    def _create_object_database(self):
        database = DatabaseConnection(self.database_name)
        self.connection = database.create_connect()
        self.database_manager = DatabaseManager(self.connection)
        
    def get_songs(self, answer):
        self._create_object_database()
        is_table_in_db = self.database_manager.ensure_table_exist(self.table_name)
        if is_table_in_db is True:
            if answer is None:
                songs = self._get_random_songs()
            else:
                vibe = answer["vibe"]
                subject = answer["subject"]
                time = answer["time"]
                songs = self._get_personalized_songs(vibe, subject, time)
            self.connection.close()
            return songs
        self.connection.close()
        return None

    def _get_personalized_songs(self, vibe, subject, time):
        return self.database_manager.create_personalized_playlist(vibe, subject, time, self.nb_songs)
    
    def _get_random_songs(self):
        return self.database_manager.create_random_playlist(self.nb_songs)



