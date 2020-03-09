from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    place = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<News {self.city} {self.url}>'
