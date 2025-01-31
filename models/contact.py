class ContactModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fio = db.Column(db.String(220), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  description = db.Column(db.String(1000), nullable=False)

  def __repr__(self):
    return f'<User {self.phone}>'