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
        
    def test_given_an_iterable__manage_results_query_returns_a_list(self):
        expected = ["a","b","c"]
        results_iterable = [["","1","a"],["","2","b"],["","3","c"]]
        connection = MagicMock()
        db = DatabaseManager(connection)
        result = db._manage_results_query(results_iterable)
        self.assertEqual(expected, result)
        
    @mock.patch('DatabaseManager.DatabaseManager._manage_results_query', return_value=["song"])
    def test_3_create_random_playlist(self, song):
        expected = ["song"]
        nb_max_songs = Mock()
        connection = MagicMock()
        db = DatabaseManager(connection)
        result = db.create_random_playlist(nb_max_songs)
        self.assertEqual(expected, result)
    
    @mock.patch('DatabaseManager.DatabaseManager._manage_results_query', return_value=["song"])
    def test_4_create_random_playlist(self, song):
        nb_max_songs = Mock()
        connection = MagicMock()
        db = DatabaseManager(connection)
        db.create_random_playlist(nb_max_songs)
        db._manage_results_query.assert_called_once()
     
    @mock.patch('DatabaseManager.DatabaseManager._query_random_songs', return_value=["song"])
    @mock.patch('DatabaseManager.DatabaseManager._manage_results_query', return_value=["song"])
    def test_5_create_random_playlist(self, song, results):
        nb_max_songs = Mock()
        connection = MagicMock()
        db = DatabaseManager(connection)
        db.create_random_playlist(nb_max_songs)
        db._query_random_songs.assert_called_once()

if __name__ == '__main__':
    main()
