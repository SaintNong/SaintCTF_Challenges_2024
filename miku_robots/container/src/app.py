from flask import Flask, request, make_response, render_template, abort

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="")
    return app

app = create_app()

is_miku = False

@app.errorhandler(401)
def forbidden(error):
    response = make_response(render_template('401.html'))
    response.headers['X-Forwarded-Miku'] = "saint{y0u_4sk3d_s0_n1c31y}"
    return response, 401

@app.route('/')
def index():
    admin = request.cookies.get('is_miku')
    response = make_response(render_template('index.html'))

    if not admin:
        response.set_cookie('is_miku', 'false')

    response.headers['X-Forwarded-Miku'] = "saint{y0u_4sk3d_s0_n1c31y}"
    return response

@app.route('/waow')
def waow():
    response = make_response(render_template('waow.html'))
    response.headers['X-Forwarded-Miku'] = "saint{y0u_4sk3d_s0_n1c31y}"
    return response

@app.route('/admin')
def admin():
    admin = request.cookies.get('is_miku')
    if admin and admin != "false":

        response = make_response(render_template('admin.html'))
        response.headers['X-Forwarded-Miku'] = "saint{y0u_4sk3d_s0_n1c31y}"
        return response
    else:
        abort(401)



app.run(host="0.0.0.0", port=3002, debug=False)