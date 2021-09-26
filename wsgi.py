from app.main import db, app
if __name__ == '__main__':
    app.run()
    db.create_all()
