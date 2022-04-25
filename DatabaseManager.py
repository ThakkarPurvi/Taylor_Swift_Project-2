import mysql.connector
import sys


class DatabaseManager(): 

    def __init__(self, connection):
        self.connection = connection
        #self.playlist_length_limit = playlist_length_limit
        #self.cur = self.connection.cursor()

    def read_all_table_items(self, table_name):
        if self.__ensure_table_exist(table_name) is True:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM %s" % table_name)
            result = cur.fetchall()
            cur.close()
            for row in result:
                print(row)

    def query_songs(self):
        query = """ SELECT  m.PK_SongID, m.Spotify_ID,  m.Title from master_song_list m \
                INNER JOIN key_words k on m.PK_SongID=k.FK_SongID \
                where k.vibeID  = "IC" and k.SubjectID = "EX" \
                ORDER BY RAND() LIMIT 3; """
        cur = self.connection.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        for row in results:
            print(row, type(row))

    def create_playlist(self):
        pass

    def __ensure_table_exist(self, table_name):
        cur = self.connection.cursor()
        cur.execute("SHOW TABLES")
        tables = []
        for table in cur:
            tables.append(table[0])
        cur.close()
        if table_name in tables:
            return True
        else:
            return False


