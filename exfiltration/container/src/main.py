from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.get("/")
def index(code='print("Hello, world!")', result=None):
    return render_template("index.html", code=code, result=result)


@app.post("/")
def submit():
    code = request.form.get("code", "")
    return index(
        code,
        subprocess.run(
            ["python"],
            input=code,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ).stdout,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3008)
