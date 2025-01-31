import json
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
#from models.brief import BriefModel
#from models.contact import ContactModel


app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'

model = SQLAlchemy(app)

@app.route('/create-brief', methods=['POST'])
def createBrief():
    brief = BriefModel()
    model.session.add(brief)
    return model.session.commit()

@app.route('/create-contact', methods=['POST'])
def createContact():
    contact = ContactModel()
    model.session.add(contact)
    return model.session.commit()
'''
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
