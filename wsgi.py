from website.app import create_app,setup_db

app=create_app()
setup_db(app)

if __name__=='__main__':
  app.run(debug=True)