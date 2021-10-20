#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import os, sys, datetime
import imaplib
import requests

import tornado.web
import tornado.autoreload
import tornado.ioloop
import tornado.httpserver

from config import api_map

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hello")


class TaskHandler(tornado.web.RequestHandler):

    def initialize(self, envs):
        self.envs = envs

    def get(self):
        self.write("Generated PDF!")


if __name__ == "__main__":

    import platform

    if platform.system() == 'Windows':
        port = 8010

    parser = argparse.ArgumentParser(description='API')
    parser.add_argument('--port', '-p',
                        type=int,
                        default=port,
                        help='Port to binde (default: %s) % port')
    port = parser.parse_args().port
    pid = os.getpid()

    print("main pid : %s\n" % pid)
    print("listening : %s\n" % port)

    envs = {
        'cmd_map': api_map
    }

    if len(sys.argv) == 1:
        print(sys.argv)
        application = tornado.web.Application([
            (r'/', MainHandler),
            (r'/pdf', TaskHandler, dict(envs=envs))
        ])

        application.listen(port)
        tornado.ioloop.IOLoop.current().start()
