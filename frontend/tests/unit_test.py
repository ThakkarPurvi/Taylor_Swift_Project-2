from application import app
from application.routes import backend_host
from flask import url_for
from flask_testing import TestCase
import requests_mock

test_data = {
    "id": 1,
    "name": "Test UserProfile 1",
    "songs": [
        {
            "id": 1,
            "song_category": "Red Songs",
            "song_description": "Tring to test songs",
            "user_profile_id": 1
        }
    ]
}


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app


class TestViews(TestBase):

    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/get/alluserprofiles", json={'userprofiles': []})
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_home_create_userprofile(self):
        response = self.client.get(url_for('create_UserProfile'))
        self.assert200(response)


class TestHome(TestBase):

    def test_home_read_userprofile(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/get/allUser_Profiles", json={'User_Profiles': [test_data]})
            response = self.client.get(url_for('home'))
            self.assertIn("Test User_Profile 1", response.data.decode("utf-8"))


class TestCreateUser_Profile(TestBase):

    def test_create_User_Profile_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/create/userprofile", text="Test response")
            m.get(f"http://{backend_host}/get/alluserprofiles", json={'userprofiles': [test_data]})
            response = self.client.post(url_for('create_userprofile'), follow_redirects=True)
            self.assertIn("Test UserProfile 1", response.data.decode("utf-8"))


class TestCreateSong(TestBase):

    def test_create_song_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/create/song/1", text="Test response")
            m.get(f"http://{backend_host}/get/alluserprofiles", json={'userprofiles': [test_data]})
            response = self.client.post(url_for('create_song'), follow_redirects=True), json = {"userprofile": 1,
                                                                                                "song_category": "Test Song 2"}
            self.assertIn("Test UserProfile 1", response.data.decode("utf-8"))