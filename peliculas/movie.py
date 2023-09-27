from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('movie', __name__)

@bp.route('/')
def index():
    db = get_db()
    films = db.execute(
        'SELECT title, description'
        ' FROM film'
        ' ORDER BY title ASC'
    ).fetchall()
    return render_template('movie/index.html', films=films)