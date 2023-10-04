from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('movie', __name__)

@bp.route('/peliculas')
def index_films():
    db = get_db()
    films = db.execute(
        'SELECT title, description, rating, release_year'
        ' FROM film'
        ' ORDER BY title ASC'
    ).fetchall()
    return render_template('movie/peliculas.html', films=films)

@bp.route('/actores')
def index_actor():
    db = get_db()
    actors = db.execute(
        'SELECT first_name, last_name'
        ' FROM actor'
        ' ORDER BY first_name ASC'
    ).fetchall()
    return render_template('movie/actores.html', actors = actors)

@bp.route('/categorias')
def index_category():
    db = get_db()
    categories = db.execute(
        'SELECT name'
        ' FROM category'
        ' ORDER BY name ASC'
    ).fetchall()
    return render_template('movie/categorias.html', categories = categories)

@bp.route('/lenguajes')
def index_languege():
    db = get_db()
    languages = db.execute(
        'SELECT name'
        ' FROM language'
        ' ORDER BY name ASC'
    ).fetchall()
    return render_template('movie/lenguajes.html', langueges = languages)