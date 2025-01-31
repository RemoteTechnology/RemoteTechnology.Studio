class BriefModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fio = db.Column(db.String(220), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  category = db.Column(db.String(120), nullable=False)
  main_of_description = db.Column(db.String(1000), nullable=False)
  main_competitors = db.Column(db.String(1000), nullable=False)
  main_tasks = db.Column(db.String(1000), nullable=False)
  site_structure = db.Column(db.String(1000), nullable=False)
  materials = db.Column(db.String(1000), nullable=False)
  design_requirements = db.Column(db.String(1000), nullable=False)

  def __repr__(self):
    return f'<User {self.phone}>'