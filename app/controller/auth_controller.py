# app/controller/auth_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from app.model.user import UserRepo, User

bp = Blueprint("auth", __name__, url_prefix="/auth")
repo = UserRepo()

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('books.list_books'))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = repo.get_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            session['logged_in'] = True
            session['user'] = user.username
            return redirect(url_for('books.list_books'))
    return render_template("auth/login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect(url_for('index'))

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if repo.get_by_username(username):
            return render_template("auth/register.html", error="Username already exists")
        else:
            repo.add(username, password)
            return redirect(url_for("auth.login"))
    return render_template("auth/register.html")