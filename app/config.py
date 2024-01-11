import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # Get the DATABASE_URL from the environment variables
    DATABASE_URL = os.environ.get('DATABASE_URL')

    # Check if DATABASE_URL is set and modify it if necessary
    if DATABASE_URL:
        # SQLAlchemy 1.4+ no longer supports url strings that start with 'postgres://'
        # (only 'postgresql://') but Heroku's Postgres add-on sets the URL starting with 'postgres://'.
        # Hence, the connection URI must be updated here for production.
        SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace('postgres://', 'postgresql://')
    else:
        # Handle the case where DATABASE_URL is not set
        SQLALCHEMY_DATABASE_URI = None
