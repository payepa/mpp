from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

BASE_URL = "https://mppapi.vercel.app/"
# BASE_URL = "http://localhost:8000/" # Local testing

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/search")
def search():
    query = request.args.get('q')
    if query:
        results = requests.get(f"{BASE_URL}search", params={ 'q': query }).json()['results']

    return render_template('search.html', mangas=results)

@app.route("/info")
def info():
    manga_id = request.args.get('id')
    info = requests.get(f"{BASE_URL}info?id={manga_id}").json()
    
    return render_template('info.html', manga=info)

@app.route("/read")
def read():
    manga_id = request.args.get('id')
    chapter = request.args.get('chapter') or 1
    manga = requests.get(f"{BASE_URL}read?id={manga_id}&chapter={chapter}").json()

    return render_template('read.html', manga=manga)

if __name__ == "__main__":
    app.run(debug=True)

