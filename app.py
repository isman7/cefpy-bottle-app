from dashboard import Dashboard, bottle
import ConfigParser
import threading

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


class bottle_main_thread(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.host = kwargs.pop("host", "localhost")
        self.port = kwargs.pop("port", "8080")
        cfg = ConfigParser.ConfigParser()
        cfg.read(kwargs.pop("config_path", "dashboard_settings.ini"))
        self.dashboard_config = cfg
        super(bottle_main_thread, self).__init__(*args, **kwargs)

    def run(self):
        board.set_config(self.dashboard_config)
        board.main_menu.put("example", board.pages.get('example'))
        bottle.run(board, host=self.host, port=self.port, debug=True)
