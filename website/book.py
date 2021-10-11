from flask import *
from .models import User,Book
from flask_login import current_user
from time import gmtime, strftime

def secure(filename):
  time=strftime("%Y%m%d%H_%M%S", gmtime())
  return time+filename

book=Blueprint('book',__name__)

@book.route('/new')
def new_book_form():
  try:
    fname=current_user.fname
  except:
    abort(401)
  return render_template('new_book.html')
@book.route('/new',methods=["POST"])
def new_book_post():
  try:
    fname=current_user.fname
  except:
    abort(401)
  form=request.form
  f = request.files['file']
  filename=secure(f.filename)
  f.save(filename)
  newBook=Book(name=form['name'],description=form['description'],author_id=current_user.id,author=form["author"],url=filename)
  newBook.insert()
  return redirect(f'/book/display/{newBook.id}')
@book.route('/display/<int:id>')
def display_book(id):
  book=Book.query.filter_by(id=id).first()
  if not book:
    abort(404)
  return send_file("../"+book.url)

@book.route('/delete/<int:id>')
def delete_book(id):
  try:
    fname=current_user.fname
  except:
    abort(401)
  book=Book.query.filter_by(id=id).first()
  if not book:
    abort(404)
  if book.author_id==current_user.id:
    book.delete()
    flash("Kitob o'chirildi")
    return redirect('/')
  else:
    flash("Siz kitob muallfi emassiz")
    return redirect(f'/')