from flask import Flask, jsonify, render_template, redirect,request, session,flash,url_for
from flask_login import login_required,LoginManager,UserMixin, login_user, logout_user,current_user
import pandas as pd
from Route.User_route import user_bp
from Model.Thread_mode import ThreadInfo
import threading
from app.function import onelogin_login, selenium_task

app = Flask(__name__)
 
app.secret_key = 'Dheeraj@2006'
users = {
    'dheeraj@gmail.com': {'username': 'dheeraj@gmail.com', 'password': 'dheeraj@gmail.com'},
    'user2': {'username': 'user2', 'password': 'password2'}
}
login_manager = LoginManager(app)
login_manager.login_view = 'login'
class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(username):
    if username in users:
        user = User()
        user.id = username
        return user

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method=="POST":
        action=request.form['hiddenField']
        print(action)
        if action:
            return render_template('home/index.html',action=action)
    else:
        return render_template('home/index.html')

@app.route('/leads')
@login_required
def leads():
    return render_template('home/leads.html')

@app.route('/ONELEAD-LOGIN', methods=['GET', 'POST'])
@login_required
def ONLEAD_LOGIN():
    status=onelogin_login()
    return render_template('home/index.html',login=status)


@app.route('/auto-email', methods=['GET', 'POST'])
@login_required
def AUTO_EMAIL():
    if request.method=="POST":
        print("in if for threading ")
        global user_threads
        user_id = str(current_user.id)
        # Check if a thread is already running for the user
        if user_id in user_threads and user_threads[user_id].is_alive():
            data={"status":"running","message":"It's already running "}
        # Start a new thread for Selenium task for the specific user
        user_threads[user_id] = threading.Thread(target=selenium_task, args=())
        user_threads[user_id].start()
        data={"status":"success","message":"Auto email started , Check your phone for the otp and verify it  "}
        return render_template('home/auto-email.html', message=data)
    
    return render_template('home/auto-email.html')


@app.route('/auto-text', methods=['GET', 'POST'])
@login_required
def AUTO_TEXT():
    return render_template('home/auto-text.html')


@app.route('/process_text', methods=['POST'])
def process_text():
    # Get text input
    text_to_send = request.form.get('textToSend')

    # Read CSV file
    csv_file = request.files['csvFile']
    if csv_file:
        df = pd.read_csv(csv_file)

        # Print text input and DataFrame
        print("Text to Send:", text_to_send)
        print("CSV Data:")
        print(df)

    return render_template('index.html')






@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username]['password'] == password:
            user = load_user(username)
            print(user)
            login_user(user)  # Use Flask-Login's login_user to manage the user login
            flash('Login successful!', 'success')
            next_url = request.args.get('next') or url_for('index')
            return redirect(next_url)
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('home/sign-in.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already taken. Please choose a different one.', 'error')
        else:
            users[username] = {'username': username, 'password': password}
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('home/sign-up.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
