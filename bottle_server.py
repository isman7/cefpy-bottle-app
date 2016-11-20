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


@app.route('/static/<path:path>')
def server_static(path):
    """
    Enables support to CSS, JS, images, etc. Links the public URL with the real server files and serve them.
    :param path: a valid local path in server.
    :return: returns the file to bottle app.
    """
    return static_file(path, root='/'.join([abspath, 'static']))


@app.route('/home/')
def index(host="http://{}:{}".format(args.H, args.p)):
    return template('index', host=host)


@app.route('/pid/')
def pid():
    return str(os.getpid())


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == "__main__":

    bottle.run(app, host=args.H, port=args.p, debug=True)

