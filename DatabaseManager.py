import mysql.connector
import sys


class DatabaseManager(): 

    def __init__(self, connection, playlist_length_limit):
        self.connection = connection
        self.playlist_length_limit = playlist_length_limit
        #self.cur = self.connection.cursor()

    def read_all_table_items(self, table_name):
        if self.__ensure_table_exist(table_name) is True:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM %s" % table_name)
            result = cur.fetchall()
            cur.close()
            for row in result:
                print(row)

    def join_table(self):
        query = " SELECT  m.PK_SongID, m.Title from master_song_list m \
                INNER JOIN key_words k on m.PK_SongID=k.FK_SongID \
                where k.vibeID  = "IC" and k.SubjectID = "EX" \
                ORDER BY RAND() LIMIT 8; "


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


