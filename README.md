# Flask-Blog

#Requirements

1- pip install flask

2- pip install peewee


# Database Operation
Open Python Shell in Terminal

from app import *
database.create_tables([Editor, Post])

Editor.create(username='your_username', password='your_password')

Post.create(title=title, content=content)


# Start on localhost

1- flask run

Now you can login with your username/password and you can write blog post.


