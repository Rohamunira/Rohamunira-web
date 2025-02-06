from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def open_homepage():
    return render_template(
        "index.html"
    )
@app.route("/showcase")
def open_showcase():
    return render_template(
        "showcase.html"
    )
@app.route("/blog")
def open_blog():
    return render_template(
        "blog.html"
    )
@app.route("/about")
def open_about():
    return render_template(
        "about.html"
    )
if __name__ == "__main__":
    app.run(debug = True)