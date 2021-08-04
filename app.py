from flask import Flask, render_template, redirect, url_for, request, session
from peewee import *
from werkzeug.security import check_password_hash

app = Flask(__name__)
database = SqliteDatabase('database.sql')
app.secret_key = 'secret_key'



class Editor(Model):
    class Meta:
        database = database

    username = TextField()
    password = TextField()


class Post(Model):
    class Meta:
        database = database

    title = TextField()
    content = TextField()


@app.route('/')
def index():
    posts = Post.select()
    return render_template('Index.html', posts=posts)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        database_record = Editor.select().where(Editor.username == username)[0]
        hashed_password = database_record.password

        if check_password_hash(hashed_password, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('Login.html')


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/addpost', methods=['GET', 'POST'])
def newpost():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        Post.create(title=title, content=content)
        return redirect(url_for('index'))

    return render_template('New_post.html')


if __name__ == "__main__":
    app.run(debug=True)
