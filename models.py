from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(80),
                     nullable=False)
    second_name = db.Column(db.String(80),
                            nullable=False)
    email = db.Column(db.String(80),
                      unique=True, nullable=False)
    password = db.Column(db.String(150),
                         nullable=False)

    def __repr__(self):
        return f'{self.name} {self.second_name}: {self.email} {self.password}'