from flask import Flask, request, make_response, render_template, abort
import sqlite3

from flask.typing import ResponseReturnValue
con = sqlite3.connect("tutorial.db")

cur = con.cursor()
try:
    cur.execute("CREATE TABLE movie(title, year, score)")
    cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5),
            ('saint{if_sqli_is_so_good_wheres_sqli_2?}', 1969, 4.20)
    """)
except sqlite3.OperationalError:
    print('table already exists')
con.commit()


def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="")
    return app

app = create_app()


@app.errorhandler(500)
def forbidden(error):
    return render_template('500.html', error=error)


@app.route('/', methods=("POST", "GET"))
def index():
    if request.method == 'POST':
        query = request.form.get('name')
        if not query:
            query = 'a'
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()

        try:
            res = cur.execute(f"SELECT title FROM movie WHERE title = '{query}'")
        except sqlite3.OperationalError:
            return render_template('500.html', query=query), 500


        output = res.fetchall()
        return render_template('index.html', output=output)
    else:
        return render_template('index.html')
   





app.run(host="0.0.0.0", port=3003, debug=False)