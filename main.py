#!/usr/bin/env python

from google.appengine.ext import webapp

import library
import wsgiref.handlers

class Handler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("get")

  def post(self):
    self.response.out.write("post")

def main():
  app = webapp.WSGIApplication([(r".*", Handler)], debug=True)
  wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
  main()
