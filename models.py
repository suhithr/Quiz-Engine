from app import db, bcrypt

class User(db.Model):
	__tablename__= 'quizuser1'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	score = db.Column(db.Integer, nullable=False)
	answered = db.Column(db.PickleType)

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

class Questions(db.Model):
	__tablename__ = 'quizquestions1'

	question = db.Column(db.String, nullable=False)
	option1 = db.Column(db.String, nullable=False)
	option2 = db.Column(db.String, nullable=False)
	option3 = db.Column(db.String, nullable=False)
	option4 = db.Column(db.String, nullable=False)
	answer = db.Column(db.String, nullable=False)
	creatorid = db.Column(db.String, nullable=False)
	questionid = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String, nullable=False)
	difficulty = db.Column(db.String, nullable=False)

	def __init__(self, question, option1, option2, option3, option4, answer, creatorid, category, difficulty):
		self.question = question
		self.option1 = option1
		self.option2 = option2
		self.option3 = option3
		self.option4 = option4
		self.answer = answer
		self.creatorid = creatorid
		self.category = category
		self.difficulty = difficulty

	def __repr__(self):
		return "<Question id is %s and creatorid is %s" % (self.questionid, self.creatorid)