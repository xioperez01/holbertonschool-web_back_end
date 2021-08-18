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

    def valid_login(self, email: str, password: str) -> bool:
        """ Valid credentials """
        if password is None or type(password) is not str:
            return False

        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password.encode(),
                                  found_user.hashed_password)

    def create_session(self, email: str) -> str:
        """ takes an email and returns the session Id"""
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            new_uuid = _generate_uuid()
            self._db.update_user(found_user.id, session_id=new_uuid)
            return new_uuid

    def get_user_from_session_id(self, session_id: str) -> User:
        """ takes a session_id and returns
        the User or None."""
        try:
            found_user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            if found_user.session_id is None:
                return None
            return found_user

    def destroy_session(self, user_id: int) -> None:
        """ Takes a user_id and updates the
        corresponding user’s"""
        try:
            found_user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        else:
            self._db.update_user(found_user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Find the user"""
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        else:
            reset_token = _generate_uuid()
            self._db.update_user(found_user.id, reset_token=reset_token)
            return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ hash the password and update the user """
        try:
            found_user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            hashed_password = _hash_password(password)
            self._db.update_user(found_user.id,
                                 hashed_password=hashed_password)
            self._db.update_user(found_user.id, reset_token=None)
