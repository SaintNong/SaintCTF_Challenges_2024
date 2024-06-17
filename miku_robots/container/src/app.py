from flask import Flask, request, make_response, render_template, abort

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="")
    return app

app = create_app()

is_miku = False


def add_headers(template):
    response = make_response(render_template(template))
    response.headers['X-Forwarded-Miku'] = "saint{y0u_4sk3d_s0_n1c31y}"
    return response

@app.errorhandler(401)
def forbidden(error):
    response = add_headers('401.html')
    return response, 401

@app.route('/')
def index():
    admin = request.cookies.get('is_miku')
    response = add_headers('index.html')

    if not admin:
        response.set_cookie('is_miku', 'false')
    return response

@app.route('/waow')
def waow():
    response = add_headers('waow.html')
    return response

@app.route('/admin')
def admin():
    admin = request.cookies.get('is_miku')
    if admin and admin != "false":

        response = add_headers('admin.html')
        return response
    else:
        abort(401)



app.run(host="0.0.0.0", port=3002, debug=False)