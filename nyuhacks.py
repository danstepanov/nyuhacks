import tornado.ioloop
import tornado.web
#import libraries

# *** USER SUBMISSION ***
class Title():
    title = raw_input("Title: ")
		if len(input_str) > 30:
    		print "Only 30 characters allowed."
    sys.exit()

class Story():
	story = raw_input("Story: ")
		if len(input_str) > 500:
    		print "Only 500 characters allowed."
    sys.exit()

class Location():
