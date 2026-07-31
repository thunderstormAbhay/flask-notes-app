from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route("/")
def index():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note")

    if note:
        notes.append(note)

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(notes):
        notes.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
