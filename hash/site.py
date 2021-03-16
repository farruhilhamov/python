#!/usr/bin/env python

import flask
import os


# Create the application.
APP = flask.Flask(__name__)

template = "index2.html"
print("\n")    
print("file existing is ",os.path.exists(template))    
print("\n")    

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template(template)


if __name__ == '__main__':
    APP.debug=True
    APP.run()