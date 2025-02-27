from flask import Flask, render_template
app = Flask(__name__, static_folder="static")

@app.route("/")
def load_index():
    return render_template("/index.html")

@app.route("/hashmaps")
def load_hashmaps():
    return render_template("/hashmaps.html")


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
