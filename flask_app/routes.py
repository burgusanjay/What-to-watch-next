from requests import request
from flask import render_template, url_for, flash, redirect
from flask_app.forms import addcontent
from flask_app.models import Movies, Series
from flask_app import app, db


@app.route('/')
@app.route('/home')
def hello():
    movies = Movies.query.all()
    series = Series.query.all()
    return render_template('home.html', movies=movies, series=series)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = addcontent()
    if request.method == 'POST' and form.validate():
        if form.type == 'Movies':
            content = Movies(title=form.title.data)
            db.session.add(content)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('home'))
        if form.type == 'Series':
            content = Series(title=form.title.data)
            db.session.add(content)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('home'))
    return render_template('post_content.html', title='Post Content',
                               form=form, legend='Post Content')