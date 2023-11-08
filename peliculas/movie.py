from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('movie', __name__)

@bp.route('/peliculas')
def index_films():
    db = get_db()
    db.execute(
        'SELECT title, description, rating, release_year, film_id'
        ' FROM film'
        ' ORDER BY title ASC'
    )
    films = db.fetchall()
    return render_template('movie/peliculas.html', films=films)

@bp.route('/api/peliculas')
def index_films_api():
    db = get_db()
    db.execute(
        'SELECT title, description, rating, release_year, film_id'
        ' FROM film'
        ' ORDER BY title ASC'
    )
    films = db.fetchall()

    for film in films:
        film["url"] = url_for("movie.index_una_pelicula_api", id=film["film_id"], _external=True)

    return jsonify (films=films)




@bp.route('/actores')
def index_actor():
    db = get_db()
    db.execute(
        'SELECT first_name, last_name, actor_id'
        ' FROM actor'
        ' ORDER BY first_name ASC'
    )
    actors = db.fetchall()
    return render_template('movie/actores.html', actors = actors)

@bp.route('/api/actores')
def index_actor_api():
    db = get_db()
    db.execute(
        'SELECT first_name, last_name, actor_id'
        ' FROM actor'
        ' ORDER BY first_name ASC'
    )
    actors = db.fetchall()

    for actor in actors:
        actor["url"] = url_for("movie.index_un_actor_api", id=actor["actor_id"], _external=True)

    return jsonify(actors = actors)




@bp.route('/categorias')
def index_category():
    db = get_db()
    db.execute(
        'SELECT name'
        ' FROM category'
        ' ORDER BY name ASC'
    )
    categories = db.fetchall()
    return render_template('movie/categorias.html', categories = categories)

@bp.route('/api/categorias')
def index_category_api():
    db = get_db()
    db.execute(
        'SELECT name'
        ' FROM category'
        ' ORDER BY name ASC'
    )
    categories = db.fetchall()
    return jsonify(categories = categories)




@bp.route('/lenguajes')
def index_languege():
    db = get_db()
    db.execute(
        'SELECT name'
        ' FROM language'
        ' ORDER BY name ASC'
    )
    languages = db.fetchall()
    return render_template('movie/lenguajes.html', langueges = languages)

@bp.route('/api/lenguajes')
def index_languege_api():
    db = get_db()
    db.execute(
        'SELECT name'
        ' FROM language'
        ' ORDER BY name ASC'
    )
    languages = db.fetchall()
    return jsonify(langueges = languages)



@bp.route('/actor/<int:id>/')
def index_un_actor(id):
    db = get_db()
    actor = db.execute(
        """SELECT a.first_name, a.last_name FROM actor a
            WHERE a.actor_id = ?""",
        (id,)
    ).fetchone()

    peliculas = db.execute(
        """SELECT f.title, f.film_id
         FROM film f JOIN film_actor fa ON f.film_id = fa.film_id
         WHERE fa.actor_id = ?""",
        (id,)
    ).fetchall()
    return render_template('pagDatos/actor.html', actor = actor, peliculas = peliculas)

@bp.route('/api/actor/<int:id>/')
def index_un_actor_api(id):
    db = get_db()
    actor = db.execute(
        """SELECT a.first_name, a.last_name FROM actor a
            WHERE a.actor_id = ?""",
        (id,)
    ).fetchone()

    peliculas = db.execute(
        """SELECT f.title, f.film_id
         FROM film f JOIN film_actor fa ON f.film_id = fa.film_id
         WHERE fa.actor_id = ?""",
        (id,)
    ).fetchall()
    return jsonify(actor = actor, peliculas = peliculas)






@bp.route('/pelicula/<int:id>/')
def index_una_pelicula(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT title FROM film f
            WHERE f.film_id = ?""",
        (id,)
    ).fetchone()
    
    actores = db.execute(
        """SELECT a.first_name, a.last_name, a.actor_id FROM film_actor fa JOIN actor a ON a.actor_id = fa.actor_id  
    WHERE fa.film_id = ?""",
        (id,)
    ).fetchall()
    return render_template('pagDatos/pelicula.html', pelicula = pelicula, actores = actores)

@bp.route('/api/pelicula/<int:id>/')
def index_una_pelicula_api(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT title FROM film f
            WHERE f.film_id = ?""",
        (id,)
    ).fetchone()
    
    actores = db.execute(
        """SELECT a.first_name, a.last_name, a.actor_id FROM film_actor fa JOIN actor a ON a.actor_id = fa.actor_id  
    WHERE fa.film_id = ?""",
        (id,)
    ).fetchall()
    return jsonify(pelicula = pelicula, actores = actores)