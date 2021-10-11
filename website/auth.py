from flask import * 
from .models import User
from flask_login import login_user,current_user,logout_user
from .app import db

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET'])
def login_form():
  return render_template('login.html')

@auth.route('/login',methods=["POST"])
def login():
    form=request.form
    user=User.query.filter_by(username=form["username"], password=form['password']).first()
    if not user:
      flash('Foydalanuvchi topilmadi!')
      return render_template('login.html')
    login_user(user)
    flash("Hisobingizga kirdingiz")
    return redirect('/')

@auth.route('/signup',methods=['GET'])
def signup_form():
  return render_template('signup.html')

@auth.route('/signup',methods=["POST"])
def signup():
  form=request.form
  newUser=User(fname=form['fname'],lname=form['lname'],email=form['email'],password=form['password'],username=form['username'])
  try:
    newUser.insert()
    flash("Hisob yaratildi")
    return redirect('/')
  except Exception as e:
    print(e)
    flash("Nimadur xato bo'ldi!<br>Ma'lumotlaringizni tekshirib ko'ring!")
    return render_template('signup.html')
@auth.route('/logout')
def logout():
  try:
    logout_user()
  except:
    a=0
  return redirect('/auth/login')


@auth.route('/profile')
def profile():
  try:
    fname=current_user.fname
    return render_template('profile.html',user=current_user,auth=True)
  except:
    abort(401)

@auth.route('/settings')
def settings():
  try:
    fname=current_user.fname
    return render_template('settings.html',user=current_user,auth=True)
  except:
    abort(401)
@auth.route('/settings',methods=["POST"])
def settings_post():
  try:
    fname=current_user.fname
  except:
    abort(401)
  form=request.form
  user=User.query.filter_by(id=current_user.id)
  user.fname=form['fname']
  user.lanme=form['lname']
  user.email=form['email']
  current_user.fname=form['fname']
  current_user.lanme=form['lname']
  current_user.email=form['email']
  db.session.commit()
  flash("Ma'lumotlar o'zgartirildi")
  return redirect('/auth/profile')


  
  



