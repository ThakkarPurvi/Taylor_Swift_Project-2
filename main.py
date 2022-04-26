from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager


def main():
    database_name = "taylor_swift_project"
    table_name = "master_song_list"
    vibe = "IC"
    subject = "EX"
    database = DatabaseConnection(database_name)
    connection = database.create_connect()
    database_manager = DatabaseManager(connection)
    database_manager.query_songs(vibe, subject, 3)
    database_manager.create_query(vibe,subject, 1)
    connection.close()

if __name__ == "__main__":
    main()