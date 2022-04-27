from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import UserProfile
from application.models import Song

test_userprofile = {

    "id": 1,
    "name": "UserProfile 1",
    "songs": []

}
test_song = {
    "id": 1,
    "song_category": "Song 1",
    "song_description": "Song 1",
}


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        # Create table schema
        db.create_all()
        db.session.add(UserProfile(userprofile_name="UserProfile 1"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):
    def test_read_all_userprofiles(self):
        response = self.client.get(url_for("read_all_userprofiles"))
        all_userprofile = {"userprofiles": [test_userprofile]}
        self.assertEquals(all_userprofiles, response.json)

    def test_read_userprofiles(self):
        response = self.client.get(url_for("read_userprofile", id=1))
        json = {"userprofile_name": "User Profile 1", "id": 1}
        self.assertEquals(json, response.json)


class TestCreate(TestBase):
    def test_add_userprofile(self):
        response = self.client.post(
            url_for("add_userprofile"),
            json={"userprofile_name": "Testing add functionality"},
            follow_redirects=True
        )
        self.assertEquals(b"Added New User Profile: Testing add functionality", response.data)


class TestUpdate(TestBase):
    def test_update_userprofile(self):
        response = self.client.put(
            url_for("update_userprofile", id=1),
            json={"name": "Testing update functionality"}
        )
        self.assertEquals(b"Updated UserProfile ID: 1 ", response.data)


class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.delete(url_for("delete_userprofile", id=1))
        self.assertEquals(b"Deleted UserProfile with ID: 1 ", response.data)
        self.assertIsNone(Country.query.get(1))