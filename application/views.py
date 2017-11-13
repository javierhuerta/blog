from application import app
from flask import render_template, request, redirect, url_for
from application.models import Post
from application.database import db_session
import datetime

@app.route('/')
def index():
    return render_template(
        'index.html'
        )    


@app.route('/posts')
def posts():
    ctx = {}
    posts = Post.query.order_by("id desc")
    ctx['posts'] = posts

    return render_template(
        'posts.html', 
        ctx = ctx
        )


@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    ctx = {
        'message': 'Add a new post',
        'form_is_ok': True
    }
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        if title and body:
            # If title and body exists
            p = Post(
                title=title, 
                body=body, 
                pub_date=datetime.datetime.now().date()
            )

            db_session.add(p)
            db_session.commit()

            # Return redirect to posts view
            return redirect(url_for('posts'))

        else:
            ctx['message'] = 'Error on form'
            ctx['form_is_ok'] = False  

    return render_template(
        'new_post.html',
        ctx = ctx
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html'
    )


@app.route('/about')
def about():
    return render_template(
        'about.html'
    )