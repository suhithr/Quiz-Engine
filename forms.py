from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(Form):
	name = TextField(
		'name',
		validators=[DataRequired()]
	)
	username = TextField(
		'username',
		validators=[DataRequired(), Length(min=3, max=25)]
	)
	password = PasswordField(
		'password',
		validators=[DataRequired(), Length(min=3, max=25)]
	)
	confirm = PasswordField(
		'confirm',
		validators=[DataRequired(), EqualTo('password', message='Passwords must match.')]
	)

class LoginForm(Form):
	username = TextField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

class SubmitForm(Form):
	question = TextField('question', validators=[DataRequired()])
	option1 = TextField('option1', validators=[DataRequired()])
	option2 = TextField('option2', validators=[DataRequired()])
	option3 = TextField('option3', validators=[DataRequired()])
	option4 = TextField('option4', validators=[DataRequired()])
	answer = SelectField(
		'answer', 
		choices=[('option1', 'A'), ('option2', 'B'), ('option3', 'C'), ('option4', 'D')], 
		validators=[DataRequired()]
	)
	category = SelectField(
		'category', 
		choices=[('math', 'Math'), ('pop_culture', 'Pop Culture'), ('history', 'History'), ('sports', 'Sports'), ('business', 'Business'), ('tech', 'Technology'), ('geography', 'Geography'), ('other', 'Other')], 
		validators=[DataRequired()]
	)
	difficulty = SelectField(
		'Difficulty', 
		choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('hard', 'Hard'), ('insane', 'Insane')],
		validators=[DataRequired()]
	)

class QuizForm(Form):
	attempted_answer = SelectField(
		'attempt',
		choices=[('option1', 'A'), ('option2', 'B'), ('option3', 'C'), ('option4', 'D')],
		validators=[DataRequired()]
	)