from flask import Flask, render_template, request
from summarizer import summarize_youtube_video 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    error = None
    if request.method == "POST":
        url = request.form.get("youtube_url")
        try:
            summary = summarize_youtube_video(url)
        except Exception as e:
            error = str(e)
    return render_template("index.html", summary=summary, error=error)

if __name__ == "__main__":
    app.run(debug=True)
