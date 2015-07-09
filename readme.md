##Quiz Engine
This project is packaged as a **Flask** App with a PostgreSQL Database and SQLAlchemy ORM. It's a quiz platform with crowdsourced questions. Users get points for answering questions correctly and can check their position against other site users. Users can also submit their own questions to the site.

Be sure to check your score section when you get the most number of points. Hint: :crown:

**Tech Used**

Client Side:

* HTML with Jinja2 Templating, CSS, JavaScript
* [MaterializeCSS](http://wwwmaterializecss.com) (Loaded with CDN)
* [JQuery 1.11.3](https://www.jquery.com) (Loaded with CDN)

Server Side:

* [Flask](http://flask.pocoo.org)
* [PostgreSQL](http://www.postgresql.org/)
* [SQLAlchemy](http://www.sqlalchemy.org/)

Note: The modules required recorded with `pip freeze` are in [requirements.txt](https://github.com/suhithr/Quiz-Engine/blob/master/requirements.txt).

**Server Routes:**

*Open Routes*

* '/' - Home
* '/login' - Login
* '/logout' - Logout
* '/register' - Register

*Protected Routes*

* '/quiz' - Questions Displayed for User to Answer
* '/quiz/<category>' - Questions of the specified category displayed, the category must be one of ['math','pop_culture','history','sports','business','tech','geography','other']
* '/score' - To see the standings among users
* '/submit' - Where users can submit questions of their own

**Tables**

The database contains 2 tables. The table 'quizuser1' is from the User class, and the table 'quizquestions1' is from the Questions class. These classes are from [models.py](https://github.com/suhithr/Quiz-Engine/blob/master/models.py)

* User -> [id, name, username, password, score, answered]
* Questions -> [question, option1, option2, option3, option4, answer, creatorid, questionid, category, difficulty]

Note: All fields are either simple Integer or String except 'answered' in the User class. It is [pickletype](http://docs.sqlalchemy.org/en/rel_1_0/core/type_basics.html#sqlalchemy.types.PickleType) used to hold the python list which is used to maintain which questions a user has already answered.

**Modules:**

* [Flask](http://flask.pocoo.com) - `pip install Flask`
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org)  - `pip install Flask-SQLAlchemy`
* psycopg2 - `pip install psycopg2` Note that it requires PostgreSQL to be installed first, can install [PostgreSQL from](http://www.postgresql.org/)
* SQLAlchemy - `pip install sqlalchemy`
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.org/en/latest/) - `pip install flask-bcrypt` for Password Hashing
* [Flask-Login](https://flask-login.readthedocs.org/en/) - `pip install flask-login` for handling user logins
* [Flask-Migrate](https://flask-migrate.readthedocs.org/en/latest/) - `pip install flask-migrate` for handling database migrations
* [Flash-WTF](http://flask-wtf.readthedocs.org/) - `pip install flask-wtforms` for handling forms
* [WTForms](http://wtforms.readthedocs.org/) - `pip install wtforms` requirement for Flask-WTF
* Python-Bcrypt - `pip install python-bcrypt` requirement for Flask-Bcrypt

It's recommend you install all these in a virtual environment `pip install virtualenv`

**Build Instructions:**

* Set up the virtual environment by installing the required dependencies.
* Copy the repository to the appropriate folder
* Create a `config.py` file in the application root  with contents
```
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'YOUR_SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'the_URI_OF_YOUR_DATABASE'
    WTF_CSRF_SECRET_KEY = 'SECRET_KEY'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True #This makes the login_required decorator get ignored

#To be sure that it's not running in DEBUG on a Production Server
class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
```

* Change the line in `app.py` `app.config.from_object("config.ProductionConfig")` to `app.config.from_object("config.DevelopmentConfig")`
* Run `$ python db_create.py`
* Run `$ python app.py`

The app should be accessible from [localhost:5000/](localhost:5000/)

**Installing PostgreSQL**

* To install PostgreSQL follow the instructions on the link provided above for your respective operating system
* In `config.py` you must define your URI which will be of format `postgresql://username:password@localhost:port/database`
* Note: By default postgres installs with user "postgres", which you can access with `$ sudo -i -u postgres`, you can change the password with `$ sudo passwd postgres` 
* Note: Postgres terminal psql can be accessed by typing `$ psql` while logged in as an authorised user

**Screenshots:**
* ![Homepage](/screenshots/homepage.png)
* ![HomepageMobile](/screenshots/home-mobile.png)
* ![Login](/screenshots/login.png)
* ![Quiz](/screenshots/quiz.png)
* ![ScoreBoard](/screenshots/scoreboard.png)
* ![Submit Questions](/screenshots/submit.png)
* ![Quiz Category](/screenshots/quizmath.png)
* ![Register](/screenshots/register.png)

**Scoring**

Scores depend on the difficulty of the question set during question submission

* Easy +1/-1
* Moderate +2/-1
* Hard +3/-1
* Insane +4/-1


