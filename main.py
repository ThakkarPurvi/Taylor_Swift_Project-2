from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager


def main():
    database_name = "taylor_swift_project"
    table_name = "master_song_list"
    database = DatabaseConnection(database_name)
    connection = database.create_connect()
    database_manager = DatabaseManager(connection)
    database_manager.read_all_items_table(table_name)
    connection.close()

if __name__ == "__main__":
    main()