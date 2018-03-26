creating a virtual enviroment for python 3

$ python3 -m venv venv

using the virtual enviroment

$ source venv/bin/activate

installing flask

(venv) $ pip install flask

setting the FLASK_APP environment variable

(venv) $ export FLASK_APP=microblog.py

running the web application

(venv) $ flask run


Introducing  to Flask-WTF

(venv) $ pip install flask-wtf