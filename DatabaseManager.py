import mysql.connector


class DatabaseManager(): 

    def __init__(self, connection):
        self.connection = connection
        self.table_name = None
        
    def _query_songs(self, vibe, subject, nb_max_songs):
        query = """ 
            SELECT  PK_SongID, Spotify_ID, Title from {table_name} 
            INNER JOIN key_words on PK_SongID=FK_SongID 
            where vibeID  = "{vibe_id}" and SubjectID = "{subject_id}" 
            ORDER BY RAND() 
            LIMIT {nb_max_songs}; 
            """.format(table_name = self.table_name, vibe_id=vibe, subject_id=subject, nb_max_songs=nb_max_songs)
        results =  self._fetch_database(query)
        return results
    
    def _query_random_songs(self, nb_max_songs):
        query = """ 
            SELECT  PK_SongID, Spotify_ID,  Title from {table_name} \
            INNER JOIN key_words on PK_SongID=FK_SongID \
            ORDER BY RAND() \
            LIMIT {nb_max_songs}; 
            """.format(table_name = self.table_name, nb_max_songs=nb_max_songs)
        results =  self._fetch_database(query)
        return results

    def _fetch_database(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        return results
    
    def create_personalized_playlist(self, vibe, subject, nb_max_songs):
        results = self._query_songs(vibe, subject, nb_max_songs)
        list_of_songs = self._manage_results_query(results)
        return list_of_songs
            
    def create_random_playlist(self, nb_max_songs):
        results = self._query_random_songs(nb_max_songs)
        list_of_songs = self._manage_results_query(results)
        return list_of_songs
    
    def _manage_results_query(self, results):
        list_of_songs = []
        for result in results:
            list_of_songs.append(result[2])
        return list_of_songs
    
    def ensure_table_exist(self, table_name):
        cur = self.connection.cursor()
        cur.execute("SHOW TABLES")
        tables = []
        for table in cur:
            tables.append(table[0])
        cur.close()
        if table_name in tables:
            self.table_name = table_name
            return True
        else:
            return False
