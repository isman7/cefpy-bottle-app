from bottle import Bottle, template
import bottle
import os
import argparse

app = Bottle()


@app.route('/hello')
@app.route('/hello/<name>')
def index(name='World'):
    return template('hello_template', name=name)


@app.route('/pid/')
def pid():
    return str(os.getpid())


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-H', help='Server. I. e. \'localhost\'', default='localhost')
    parser.add_argument('-p', help='Port. I. e. \'8080\'', default='8080')
    args = parser.parse_args()

    bottle.run(app, host=args.H, port=args.p, debug=True)

