import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import logging

import datetime

import os.path

import random
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

class BaseHandler(tornado.web.RequestHandler):

    response = {}

    def _async(self, response = False, error = False):
        if error:
            print(error)

    def _respond(self):
        self.write(tornado.escape.json_encode(self.response))
        print tornado.escape.json_encode(self.response)
        self.finish()

    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = asyncmongo.Client(pool_id='test_pool', host='paulo.mongohq.com', port=10009, dbuser="heroku", dbpass="moistbiscuit", dbname="app19552629", maxcached=10, maxconnections=1000)
        return self._db

    @property
    def http(self):
        self._http = tornado.httpclient.AsyncHTTPClient()
        return self._http

    def generate_id(self):
        return hashlib.sha224(str(random.random())).hexdigest()[0:11];

class MainHandler(BaseHandler):
	@tornado.web.asynchronous
	def get(self):
		stories = range(100)
		for x in range(100):
			story = {
			"id": str(x),
        	"title": str(random.randrange(1000)),
        	"body": str(random.randrange(1000000000000000)),
	        "location": [random.randrange(100), random.randrange(100)],
	        "flags": 0}
		self.render("index.html")

# Input stories
	# Title
	# Story
	# Location (lat and lng)
# Pull a collection of stories
	# Based on a certain distance around you
# Be able to flag a story

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