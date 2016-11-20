from cefpython3 import cefpython as cef
from urllib import urlopen
import sys
import subprocess
import argparse


def main(arguments):
    subprocess.Popen(["python", "bottle_server.py", "-H", arguments.H, "-p", arguments.p])
    print("CEF Python {ver}".format(ver=cef.__version__))
    print("Python {ver}".format(ver=sys.version[:6]))
    assert cef.__version__ >= "53.1", "CEF Python v53.1+ required to run this"
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    browser = cef.CreateBrowserSync(url="http://{0}:{1}/home/".format(arguments.H, arguments.p))
    browser.SetClientHandler(ClientHandler(host=arguments.H, port=arguments.p))
    cef.MessageLoop()
    cef.Shutdown()


class ClientHandler(object):

    def __init__(self, **kwargs):
        self.host = kwargs.pop("host", "localhost")
        self.port = kwargs.pop("host", "8080")

    def OnBeforeClose(self, browser):
        """Called just before a browser is destroyed."""
        serverpid = urlopen("http://{0}:{1}/pid/".format(self.host, self.port)).read()
        subprocess.Popen('kill {0}'.format(serverpid), shell=True)
        if not browser.IsPopup():
            # Exit app when main window is closed.
            cef.QuitMessageLoop()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-H', help='Host. I. e. \'localhost\'', default='localhost')
    parser.add_argument('-p', help='Port. I. e. \'8080\'', default='8080')
    args = parser.parse_args()

    main(args)
