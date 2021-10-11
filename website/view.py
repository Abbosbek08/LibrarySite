from flask import *
from flask_login import current_user,login_required
from .models import Book

view=Blueprint('view',__name__)

@view.route('/')
def index():
  books=Book.query.order_by(Book.id.desc()).all()
  try:
    if current_user.fname=='':
      return render_template('index.html',books=books)
    else:
      return render_template('index.html',books=books,auth=True)
  except:
    return render_template('index.html',books=books)

def toLower(text):
  return text.lower()

@view.route('/',methods=["POST"])
def search():
  q=request.form['q']
  books1=Book.query.order_by(Book.id.desc()).all()
  books=[book for book in books1 if q in toLower(book.name) or q in toLower(book.description) or q in toLower(book.author)]
  try:
    if current_user.fname=='':
      return render_template('index.html',books=books)
    else:
      return render_template('index.html',books=books,auth=True)
  except:
    return render_template('index.html',books=books)