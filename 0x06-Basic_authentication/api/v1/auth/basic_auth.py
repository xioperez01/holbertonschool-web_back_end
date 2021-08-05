#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication class"""


def extract_base64_authorization_header(self,
                                        authorization_header: str) -> str:
    """returns the Base64 part of the
    Authorization header for an Authentication """
    if authorization_header is None:
        return None
    if type(authorization_header) is not str:
        return None
    if authorization_header[0:6] != 'Basic ':
        return None
    basic = authorization_header.split(' ', 1)[1]
    return basic
