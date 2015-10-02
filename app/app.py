from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

users = ['Ravi', 'xiaomins', 'xiaohan']
passwords = {'Ravi' : '123', 'xiaomins' : '123', 'xiaohan' : '123'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    user = request.form['username']
    password = request.form['password']
    if not user in users:
        return render_template('index.html', user_not_exist=1)
    if passwords[user] != password:
        return render_template('index.html', password_wrong=1)
    return render_template('message.html', user=user)

@app.route('/logout', methods=['GET'])
def logout():
    return render_template('index.html', logout=1)

if __name__ == '__main__':
    app.debug = True
    app.run()