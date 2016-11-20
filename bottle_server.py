from bottle import Bottle, template, static_file
import bottle
import os
import argparse


# Looking for arguments "-H" for host and "-p" for port. argparse deals with "-h" help argument automatically.
parser = argparse.ArgumentParser()
parser.add_argument('-H', help='Server. I. e. \'localhost\'', default='localhost')
parser.add_argument('-p', help='Port. I. e. \'8080\'', default='8080')
args = parser.parse_args()

# Creating a Bottle app instance.
app = Bottle()

# Using os module to know were the server is running.
abspath = os.path.abspath(".")
print "The absolute path to server program is: {}".format(abspath)

# Bottle Functions start here #


@app.route('/static/<filename>')
@app.route('/static/<type_path>/<filename>')
def server_static(type_path, filename):
    """
    Enables support to CSS, JS, images, etc. Links the public URL with the real server files and serve them.
    :param type_path: "css", "img", "js" or "fonts".
    :param filename: a valid filename in server.
    :return: returns the file to bottle app.
    """
    return static_file(filename, root='/'.join([abspath, 'static', type_path]))


@app.route('/hello')
@app.route('/hello/<name>')
def index(name='World', host="http://{}:{}".format(args.H, args.p)):
    return template('hello_template', name=name, host=host)


@app.route('/pid/')
def pid():
    return str(os.getpid())


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == "__main__":

    bottle.run(app, host=args.H, port=args.p, debug=True)

