from flask import Flask,render_template

app = Flask(__name__)


@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/jpz1')
def jpz1():  # put application's code here
    return render_template('jpz1.html')

@app.route('/jpz2')
def jpz2():  # put application's code here
    return render_template('jpz2.html')

@app.route('/jpz3')
def jpz3():  # put application's code here
    return render_template('jpz3.html')

@app.route('/jpz4')
def jpz4():  # put application's code here
    return render_template('jpz4.html')

@app.route('/jpz5')
def jpz5():  # put application's code here
    return render_template('jpz5.html')

@app.route('/nxz1')
def nxz1():  # put application's code here
    return render_template('nxz1.html')

@app.route('/nxz2')
def nxz2():  # put application's code here
    return render_template('nxz2.html')

@app.route('/nxz3')
def nxz3():  # put application's code here
    return render_template('nxz3.html')

@app.route('/nxz4')
def nxz4():  # put application's code here
    return render_template('nxz4.html')

@app.route('/nxz5')
def nxz5():  # put application's code here
    return render_template('nxz5.html')

@app.route('/acz1')
def acz1():  # put application's code here
    return render_template('acz1.html')

@app.route('/acz2')
def acz2():  # put application's code here
    return render_template('acz2.html')

@app.route('/acz3')
def acz3():  # put application's code here
    return render_template('acz3.html')

@app.route('/acz4')
def acz4():  # put application's code here
    return render_template('acz4.html')

@app.route('/acz5')
def acz5():  # put application's code here
    return render_template('acz5.html')
if __name__ == '__main__':
    app.run()
