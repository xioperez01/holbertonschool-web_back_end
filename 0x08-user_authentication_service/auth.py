#!/usr/bin/env python3
""" Authentication Module """
from bcrypt import hashpw, gensalt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """take an email and password and return a User object."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            return self._db.add_user(email, _hash_password(password))
