from flask import Flask, render_template, request, session, url_for, redirect
from app import key
import json
import getpass
from app.summarize import summary

#/mnt/cとするとwslからwindowsのファイル見れる
bookmark_path = '/mnt/c/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/bookmarks'.format(username=getpass.getuser())


app = Flask(__name__)
app.secret_key = key.SECRET_KEY

@app.route("/")
@app.route("/index")
def index():
    # Get the json of user's Chrome bookmark.
    with open(bookmark_path, encoding='utf-8') as f:
        bookmark_data = json.load(f)

    bookmark_bar = bookmark_data['roots']['bookmark_bar']['children']
    #bookmark_bar= summary(bookmark_bar)
    return render_template('index.html', bookmark_bar=bookmark_bar)

@app.route("/summarize")
def summarize():
    # Get the json of user's Chrome bookmark.
    with open(bookmark_path, encoding='utf-8') as f:
        bookmark_data = json.load(f)

    bookmark_bar = bookmark_data['roots']['bookmark_bar']['children']
    #bookmark_bar= summary(bookmark_bar)
    return render_template('summarize.html', bookmark_bar=bookmark_bar)

@app.route('/select', methods=['POST'])
def select():
    print("aaaaaaaaaaaa")
    summarize = request.form.getlist("list_data")
    print(summarize)
    if summarize == ["True"]:
        return redirect(url_for("summarize"))
    else:
        print("a")
        return redirect(url_for("index"))