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

    def query_songs(self, vibe, subject, nb_max_songs):
        query = """ 
            SELECT  PK_SongID, Spotify_ID,  Title from master_song_list  \
            INNER JOIN key_words  on PK_SongID=FK_SongID \
            where vibeID  = '{vibe_id}' and SubjectID = '{subject_id}' \
            ORDER BY RAND() LIMIT {nb_max_songs}; 
            """.format(vibe_id=vibe, subject_id=subject ,nb_max_songs=nb_max_songs)
        cur = self.connection.cursor()
        # add try handle error expection
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        for row in results:
            print(row, type(row))
        print(type(results))
        return results


    def create_query(self, vibe, subject, nb_max_songs):
        query = "SELECT  PK_SongID, Spotify_ID,  Title from master_song_list  \
                INNER JOIN key_words  on PK_SongID=FK_SongID \
                where vibeID  = %s and SubjectID = %s \
                ORDER BY RAND() LIMIT %s;"
        adr = (vibe, subject, nb_max_songs, )
        cur = self.connection.cursor()
        cur.execute(query, adr)
        results = cur.fetchall()
        cur.close()
        for row in results:
            print(row, type(row))
        print(type(results))
        return results


    def create_playlist(self, vibe, subject, nb_max_songs):
        results = self.create_query(vibe, subject, nb_max_songs)
        playlist_title_list = []
        playlist_spotify_id_list = []
        for result in results:
            print(result[2])
            playlist_title_list.append(result[2])
            playlist_spotify_id_list.append(result[1])

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


