from application import app
from application.forms import CreateUserProfileForm, CreateSongForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "final_project_taylor_swift_backend:5000"

# Get userprofile
@app.route('/', methods=["GET"])
def home():
    userprofile = requests.get(f"http://{backend_host}/get/allUserProfiles").json()["userprofiles"]
    return render_template('index.html', title="Home", userprofiles=userprofiles)

# Create UserProfile
@app.route('/create/UserProfile', methods=["GET","POST"])
def create_UserProfile():
    form = CreateUserProfileForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/UserProfile",
            json={
                "name": form.name.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_UserProfile.html", title="Add a new UserProfile", form=form)

#Create Song
@app.route('/create/song', methods=["GET","POST"])
def create_song():
    form = CreateSongForm()

    json = requests.get(f"http://{backend_host}/get/allUserProfile").json()
    for userprofile in json["userprofiles"]:
        form.userprofile.choices.append((userprofile["id"], userprofile["name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/song/{form.userprofile.data}",
            json={
                "song_category": form.song_category.data,
                "song_description": form.song_description.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_Song.html", title="Add Song", form=form)

# Update UserProfile
@app.route('/update/userprofile/<int:id>', methods=["GET","POST"])
def update_userprofile(id):
    form = CreateUserProfileForm()
    userprofile = requests.get(f"http://{backend_host}/get/UserProfile/{id}").json()

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/userprofile/{id}",
            json={
                "name": form.name.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("update_UserProfile.html", userprofile=userprofile, title="Updated Successfully", form=form)

#Delete userprofile
@app.route('/delete/userprofile/<int:id>')
def delete_userprofile(id):
    response = requests.delete(f"http://{backend_host}/delete/userprofile/{id}")
    return redirect(url_for('home'))

#Update song
@app.route('/update/song/<int:id>', methods = ['GET', 'POST'])
def update_song(id):
    form = CreateSongForm()
    song = requests.get(f"http://{backend_host}/read/song/{id}").json()
    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/song/{id}", json={"song_description": form.song_description.data, "song_category": form.song_category.data } )
        return redirect(url_for('home'))

    return render_template("update_Song.html", song=song, form=form, title = "Update")

#Delete song
@app.route('/delete/song/<int:id>')
def delete_song(id):
    response = requests.delete(f"http://{backend_host}/delete/song/{id}")
    return redirect(url_for('home'))