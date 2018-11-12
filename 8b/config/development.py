import os

DEBUG = True
SECRET_KEY = "top secret!"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    os.path.dirname(__file__), "../data-dev.sqlite3"
)
# SQLALCHEMY_TRACK_MODIFICATIONS will be removed in the next major
# release
SQLALCHEMY_TRACK_MODIFICATIONS = False
