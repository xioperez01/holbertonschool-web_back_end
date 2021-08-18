#!/usr/bin/env python3
"""
Python Module """
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome() -> str:
    """Basic message route"""
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
