import os
import requests
from flask import Flask, render_template, request, redirect, url_for,send_from_directory, jsonify
from werkzeug import secure_filename
from cassandra.cluster import Cluster

# cluster = Cluster(['127.0.0.1'], port = 9042)
# session = cluster.connect('honey')

# UPLOAD_FOLDER = '/home/honeycomb/uploads'
UPLOAD_FOLDER = '/Users/Ryan/Documents/HoneyTmp'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'F34TF$($e34D';
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg',
                                        'jpeg', 'gif', 'csv', 'tsv'])

g_user = []
passwords = {'xiaomins' : '123'}

file_index = 1000;

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    user = request.form['username']
    password = request.form['password']
    if not user in passwords:
        return render_template('index.html', user_not_exist=1)
    if passwords[user] != password:
        return render_template('index.html', password_wrong=1)
    g_user.append(user)
    return render_template('message.html')


@app.route('/preprocessing', methods=['GET'])
def preprocessing():
    return render_template('preprocessing.html')

@app.route('/visualization', methods=['GET'])
def visualization():
    if g_user and g_user[len(g_user)-1] == 'xiaomins' :
        return render_template('knnresult.html', flag = 1)
    else:
        return render_template('knnresult.html', flag = 0)

@app.route('/register', methods=['POST'])
def register():
    user = request.form['username']
    password = request.form['password']
    re_enter_password = request.form["re_enter_password"]
    if user in passwords:
        return render_template('register.html', user_exist=1)
    if password != re_enter_password:
        return render_template('register.html', password_not_match=1)
    passwords[user] = password
    return render_template('index.html', resiter_success=1)

@app.route('/go_register', methods=['GET'])
def go_register():
    return render_template('register.html')

@app.route('/logout', methods=['GET'])
def logout():
    return render_template('index.html', logout=1)

# Route that will process the file upload
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        r = requests.get('http://128.2.7.38:32769/run')
        # files = request.files.getlist("file[]")
        # training_file = files[0]
        # testing_file = files[1]
        # if files:
            # r = requests.get('http://128.2.7.38:32769/run')
            # respond = r.status_code
            # print respond
            # training_data = secure_filename(training_file.filename)
            # testing_data = secure_filename(testing_file.filename)
            # training_file.save(os.path.join(app.config['UPLOAD_FOLDER'], training_data))
            # testing_file.save(os.path.join(app.config['UPLOAD_FOLDER'], testing_data))

        # session.execute(
        #         """
        #         INSERT INTO data (id, path)
        #         VALUES (%s, %s)
        #         """,
        #         (file_index, UPLOAD_FOLDER + '/' + training_file + ';' + UPLOAD_FOLDER + '/' + testing_file)
        #     )
    return render_template('upload.html')

if __name__ == '__main__':
    app.debug = True
    # app.run(host='128.2.7.38', port=7124)
    app.run()