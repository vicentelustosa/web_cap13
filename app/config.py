import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = "sqlite:///banco.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
