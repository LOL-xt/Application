from app.main import db, app
if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
