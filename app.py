from flask import Flask, render_template
import json

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tradeit')
def ti():
    return 'ti'

@app.route('/csgoempire')
def empire():
    with open('parsers/empire/empire.json', 'r') as j:
        data = json.loads(j.read())
    return render_template('parser.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)