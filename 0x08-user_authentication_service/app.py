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


@app.route('/users', methods=['POST'])
def users():
    """Register users"""
    req_par = request.form
    email = req_par.get('email')
    password = req_par.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        msg = {"email": new_user.email, "message": "user created"}
        return jsonify(msg)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Login users"""
    req_par = request.form
    email = req_par.get('email')
    password = req_par.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if not session_id:
            abort(401)
        msg = {"email": email, "message": "logged in"}
        output = jsonify(msg)
        output.set_cookie("session_id", session_id)
        return output
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logout users"""
    session_id_req = request.cookies.get("session_id", None)
    if not session_id_req:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id_req)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """Get profile"""
    session_id_req = request.cookies.get("session_id", None)
    if not session_id_req:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id_req)
    if user:
        msg = {"email": user.email}
        return jsonify(msg)
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Generate users reset password token"""
    req_par = request.form
    email = req_par.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    else:
        msg = {"email": email, "reset_token": token}
        return jsonify(msg)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Reset users password"""
    req_par = request.form
    email = req_par.get('email')
    reset_token = req_par.get('reset_token')
    new_password = req_par.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    else:
        msg = {"email": email, "message": "Password updated"}
        return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
