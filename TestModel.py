from unittest import mock
from unittest import TestCase, main
import io
from Model import Model
from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager


class TestModel(TestCase):

    @mock.patch('DatabaseManager.DatabaseManager.ensure_table_exist', return_value=False)
    def test_when_given_wrong_table_then_get_song_returns_None(self, value):
        expected = None
        answer = ""
        model = Model()
        result = model.get_songs(answer)
        self.assertEqual(expected, result)
        
    @mock.patch('DatabaseManager.DatabaseManager.ensure_table_exist', return_value=True)
    @mock.patch('Model.Model._get_random_songs', return_value=["song"])
    def test_1(self, song, value):
        expected = ["song"]
        answer = None
        model = Model()
        result = model.get_songs(answer)
        self.assertEqual(expected, result)
        
    @mock.patch('DatabaseManager.DatabaseManager.ensure_table_exist', return_value=True)
    @mock.patch('Model.Model._get_personalized_songs', return_value=["song"])
    def test_2(self, song, value):
        expected = ["song"]
        answer = {"vibe":"vibe", "subject":"subject"}
        model = Model()
        result = model.get_songs(answer)
        self.assertEqual(expected, result)
        
        
         decorated.deleteToDo.assert_called_once()
        
if __name__ == '__main__':
    main()
