##Quiz Engine
This project is packaged as a **Flask** App with a Postgresql Database and SQLAlchemy ORM. It's a quiz platform with crowdsourced questions. Users get points for answering questions correctly and can check their position against other site users. Users can also submit their own questions to the site.

**Tech Used**

Client Side:

* HTML with Jinja2 Templating, CSS, JavaScript
* [MaterializeCSS](http://wwwmaterializecss.com)
* [JQuery 1.11.3](https://www.jquery.com)

Server Side:

* [Flask](http://flask.pocoo.org)
* [PostgreSQL](http://www.postgresql.org/)
* [SQLAlchemy](http://www.sqlalchemy.org/)

Note: The modules required recorded with 'pip freeze' are in [requirements.txt](https://github.com/suhithr/Quiz-Engine/blob/master/requirements.txt)

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

The database contains 2 tables.

Table "quizuser1"
  Column  |       Type        |                       Modifiers                        
----------+-------------------+--------------------------------------------------------
 id       | integer           | not null default nextval('quizuser1_id_seq'::regclass)
 name     | character varying | not null
 username | character varying | not null
 password | character varying | not null
 score    | integer           | not null
 answered | bytea             | 







