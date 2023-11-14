from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#set up app to use a sqlalchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampledb.db'
db = SQLAlchemy(app)



#setup a simple table for database
class visitor(db.Model):
    username= db.Column(db.String(100), primary_key=True)
    numVisits = db.Column(db.Integer, default = 1)
    favoriteFood = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.username} - {self.numVisits}"
    

with app.app_context():
    db.create_all()


#make a homepage
@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/hello/<name>')
def hello(name):
    listofNames = [name, "yoyo", "yennifer"]
    return render_template('name.html', name = name,nameList = listofNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name=None
    if request.method == 'POST':
        name=request.form['name']
        #check if vis
        visitor1 = visitor.query.get(name)
        if visitor == None:
            #add vis
            visitor1 = visitor(username = name)
            db.session.add(visitor1)
        else:
            visitor.numVisits +=1

        db.session.commit()

    return render_template('form.html', name=name)

#add in a page to view all visators
@app.route()('/visitors')
def visitors():
    pass


# add the option to run this file directly 
if __name__ == "__main__":
    app.run(debug=True)
