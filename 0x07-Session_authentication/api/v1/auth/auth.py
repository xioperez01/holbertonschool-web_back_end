#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return false """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns none """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None """
        return None

    def session_cookie(self, request=None):
        """returns a cookie """
        if request is None:
            return None
        name_var = os.getenv('SESSION_NAME')
        value = request.cookies.get(name_var)
        return value
