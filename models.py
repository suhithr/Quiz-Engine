from app import db, bcrypt

class User(db.Model):
	__tablename__= 'quizuser1'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	score = db.Column(db.Integer, nullable=False)
	#Is it ok to let answered be nullable?
	answered = db.Column(db.String)

	def __init__(self, name, username, password, score):
		self.name = name
		self.username = username
		self.password = bcrypt.generate_password_hash(password)
		self.score = score

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return "<Username is '%s'" % (self.username)