from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def StartPage():
    #check for session
    return render_template('dashboard.html')


@app.route('/login')
def LoginPage():
    #default page
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



app.run(debug=True)