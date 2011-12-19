#!/usr/bin/env python

from google.appengine.ext import db


class Paper(db.Model):
  paper = db.ListProperty(db.key)
  sha1 = db.StringProperty(required=True)
  score = db.IntegerProperty(required=True)


class Paragraph(db.Model):
  paragraph = db.ListProperty(db.key)
  sha1 = db.StringProperty(required=True)
  score = db.IntegerProperty(required=True)


class ParagraphComparison(db.Model):
  group = db.ListProperty(db.key)


class Sentence(db.Model):
  sentence = db.ListProperty(db.key)
  sha1 = db.StringProperty(required=True)
  score = db.IntegerProperty(required=True)


class SentenceComparison(db.Model):
  group = db.ListProperty(db.key)


class Word(db.Model):
  word = db.StringProperty(required=True)
  soundex = db.StringProperty(required=True)


class User(db.Model):
  user_id = db.IntegerProperty(required=True)
  score = db.IntegerProperty(required=True)
  user_name = db.StringProperty(required=True)
  password = db.StringProperty(required=True)
  nonce = db.StringProperty(required=True)
  sign_up_date = db.DateTimeProperty(auto_now_add=True)
  status = db.IntegerProperty(required=True)


class Vote(db.Model):
  pass


class Log(db.Model):
  pass
