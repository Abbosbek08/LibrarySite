from .app import db

class User(db.Model):
  __tablename__='users'
  id=db.Column(db.Integer, primary_key=True)
  fname=db.Column(db.String,nullable=False)
  lname=db.Column(db.String,nullable=False)
  email=db.Column(db.String,nullable=False,unique=True)
  password=db.Column(db.String,nullable=False)
  username=db.Column(db.String,unique=True,nullable=False)
  authenticated = db.Column(db.Boolean, default=False)
  # is_authenticated=authenticated
  def login(self):
    self.authenticated=True
    db.session.commit()
  @property
  def is_active(self):
        """True, as all users are active."""
        return True

  def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id
  @property
  def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated
  @property
  def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
  def insert(self):
    db.session.add(self)
    db.session.commit()
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  def update(self):
    db.session.commit()
class Book(db.Model):
  __tablename__='books'
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String,nullable=False)
  description=db.Column(db.String,nullable=False)
  author_id=db.Column(db.Integer,db.ForeignKey('users.id'))
  author=db.Column(db.String,nullable=False)
  url=db.Column(db.String,nullable=False)
  def insert(self):
    db.session.add(self)
    db.session.commit()
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  def update(self):
    db.session.commit()