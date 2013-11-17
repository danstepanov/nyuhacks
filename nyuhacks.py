import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import logging

import datetime

import os.path
#import libraries

# Define Port
define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):

    def __init__(self, debug = False):
        handlers = [
            # Home page
            (r"/", MainHandler)
        ]
        settings = dict(
            cookie_secret="/Vo=",
            login_url="",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            facebook_api_key="",
            facebook_secret="",
            debug=debug
        )

        # logging.info("Static URL: {}".format(settings['static_path']))
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

# Main Runtime
def main():
    tornado.options.parse_command_line()
    logging.info("starting webserver on 0.0.0.0:%d" % tornado.options.options.port)
    print("Web server started again at "+str(datetime.datetime.now()))
    app = Application(debug = (True if options.port==8888 else False))
    app.listen(options.port)

    # Create IOLoop
    mainloop = tornado.ioloop.IOLoop

    # Create scheduled cron jobs
    interval_ms = 1000

    # Start main loop
    mainloop.instance().start()


if __name__ == "__main__": main()