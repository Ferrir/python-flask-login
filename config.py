import os.path
baserdir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(baserdir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '@#$101665&*('