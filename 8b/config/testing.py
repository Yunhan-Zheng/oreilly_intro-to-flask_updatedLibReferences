import os

DEBUG = False
TESTING = True
SECRET_KEY = "top secret!"
WTF_CSRF_ENABLED = False
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    os.path.dirname(__file__), "../data-test.sqlite3"
)
# SQLALCHEMY_TRACK_MODIFICATIONS will be removed in the next major
# release
SQLALCHEMY_TRACK_MODIFICATIONS = False
