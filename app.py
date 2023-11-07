from flask import Flask, render_template , request

app = Flask(__name__)

#make a homepage
@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/hello/<name>')
def hello(name):
    listofNames = [name, "yoyo", "yennifer"]
    return render_template('name.html', name = name,nameList = listofNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)


# add the option to run this file directly 
if __name__ == "__main__":
    app.run(debug=True)
