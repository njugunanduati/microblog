import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'just trust me'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jamonjuguna@localhost/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False