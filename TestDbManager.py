from unittest import mock
from unittest.mock import patch, Mock, MagicMock
from unittest import TestCase, main
import io
from Model import Model
from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager


class TestDatabaseManager(TestCase):

    @mock.patch('DatabaseManager.DatabaseManager._fetch_database', return_value=["song"])
    def test_1_query_songs(self, song):
        expected = ["song"]
        vibe = Mock()
        subject = Mock()
        nb_max_songs = Mock()
        connection = MagicMock()
        db = DatabaseManager(connection)
        result = db._query_songs(vibe, subject, nb_max_songs)
        self.assertEqual(expected, result)
        
    @mock.patch('DatabaseManager.DatabaseManager._fetch_database', return_value=["song"])
    def test_2_query_random_songs(self, song):
        expected = ["song"]
        nb_max_songs = Mock()
        connection = MagicMock()
        db = DatabaseManager(connection)
        result = db._query_random_songs(nb_max_songs)
        self.assertEqual(expected, result)
        
    @mock.patch('DatabaseManager.DatabaseManager._fetch_database', return_value=["song"])
    def test_3_given_an_iterable_(self, song):
        expected = ["song"]
        nb_max_songs = Mock()
        connection = MagicMock()
        db = DatabaseManager(connection)
        result = db._query_random_songs(nb_max_songs)
        self.assertEqual(expected, result)
    
        def _manage_results_query(self, results):
            list_of_songs = []
        for result in results:
            list_of_songs.append(result[2])
        return list_of_songs
    
    
if __name__ == '__main__':
    main()
