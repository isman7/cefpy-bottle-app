from dashboard import Dashboard
import bottle
import begin
import ConfigParser
import os

cfg = ConfigParser.ConfigParser()
board = Dashboard()


@board.route('/')
@board.route('/home/')
@board.route('/home', name="main_page")
@board.page('main_page')
def index():
    pass


@board.route('/page/', name="example")
@board.page('example')
def do_stuff():
    pass

@board.route('/pid/')
def pid():
    """
    Auxiliar function that reports the PID of the subprocess running
    the Bottle server in order to kill it if necessary.
    :return: a plain htlm page with the PID
    """
    return str(os.getpid())

@begin.start(auto_convert=True)
@begin.logging
def main(host='localhost', port='8080', config_path="dashboard_settings.ini"):

    cfg.read(config_path)
    board.set_config(cfg)

    board.main_menu.put("example", board.pages.get('example'))
    bottle.run(board, host=host, port=port, debug=True)

