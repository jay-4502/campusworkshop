"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7su5269vf5qbbb2ig-a.oregon-postgres.render.com",
        database="todo_rzgy",
        user="root",
        password="va9wd30MmpH1ncAOjOEAOggQVE8ORNJz")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
