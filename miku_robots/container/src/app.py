from flask import Flask, request, make_response, render_template, abort

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="")
    return app

app = create_app()

is_miku = False

@app.errorhandler(401)
def page_not_found(error):
    return render_template('401.html'), 401

@app.route('/')
def index():
    admin = request.cookies.get('is_miku')
    response = make_response(render_template('index.html'))

    if not admin:
        response.set_cookie('is_miku', 'false')

    response.headers['X-Forwarded-Miku'] = "saint{y0u_4sk3d_s0_n1c31y}"
    return response

@app.route('/waow')
def hello():
    return render_template('waow.html')

@app.route('/admin')
def admin():
    admin = request.cookies.get('is_miku')
    if admin and admin != "false":
        return render_template("admin.html")
    else:
        abort(401)



app.run(host="0.0.0.0", port=3002, debug=False)