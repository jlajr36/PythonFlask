from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/moredata', methods=['GET','POST'])
def moredata():
    if request.method == 'GET':
        return '<h1>yea</h1>'
    if request.method == 'POST':
        num = request.form["num"]
        print(num)
        return '<h1>%s</h1>' % num

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)