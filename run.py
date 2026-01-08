from flask import render_template, Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"

@app.route('/healthy')
def healthy():
    return {'status': 'enabled'}

if __name__ == '__main__':
    app.run(debug=True)
