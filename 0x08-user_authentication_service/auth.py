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
