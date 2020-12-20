from flask import Flask, render_template, redirect, request,url_for
app = Flask(__name__)

@app.route('/display', methods=['POST','GET'])
def display():
    if request.method == 'POST':
        fName = request.form['fname']
        return redirect(f"/user/{fName}")

@app.route('/user/<name>')
def user(name):
    return f"Your name is {name}"

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)