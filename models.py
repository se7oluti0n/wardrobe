from index import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

    def __repr__(self):
        return '<Item %r>' % self.name