import threading
from flask import Blueprint, flash, jsonify,request,redirect,render_template, session, url_for
from app.function import   auto_email_via_html, auto_email_via_text, auto_text, selenium_task,login_required
from ..DB.Db_config import collection
import pandas as pd
from bson.objectid import ObjectId

general_bp = Blueprint('general_bp', __name__)

all_threads=[]
@general_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method=="POST":
        action=request.form['hiddenField']
        print(action)
        if action:
            return render_template('home/index.html',action=action)
    else:
        return render_template('home/index.html')

@general_bp.route('/leads')
@login_required
def leads():
    return render_template('home/leads.html')



@general_bp.route('/auto-email', methods=['GET', 'POST'])
@login_required
def AUTO_EMAIL():
    if request.method=="POST":
        try:
            global all_threads
            all_threads = [thread for thread in all_threads if thread["Thread"].is_alive()]
            action=request.form['action']
            email_subject=request.form['emailSubject']
            email_body=request.form['emailBody']
            csv_data=request.files['csvFile']
            selected_option = request.form.get('myDropdown')
            print(selected_option)
            if csv_data:
                df = pd.read_csv(csv_data)
                df = df.dropna(subset=['Lead_url'])
                lead_url_list = df['Lead_url'].tolist()
            for t in all_threads:
                if t['Action'] == action and t['Thread'].name==session['user_id']+"_"+action and t['Thread'].is_alive():
                    print("Thread is running.")
                    print(all_threads)
                    data={"status":"running","message":"thread already running  "}
                    return render_template('home/auto-email.html', message=data)
                # If no running thread found, create a new one
            print(lead_url_list)
            # th = threading.Thread(target=selenium_task, args=(), name=session['user_id']+"_"+action)
            if selected_option=='Text':
                th = threading.Thread(target=auto_email_via_text, args=(lead_url_list,email_subject,email_body,session['user_id'],), name=session['user_id']+"_"+action)
                all_threads.append({"Action": action, "Thread": th})
                th.start()
                print("Thread is not running. Creating a new thread.")
                print(all_threads)
                data={"status":"success","message":"Auto email started , Check your phone for the otp and verify it  "}
                return render_template('home/auto-email.html', message=data)
            elif selected_option=='Html':
                th = threading.Thread(target=auto_email_via_html, args=(lead_url_list,email_subject,email_body,session['user_id'],), name=session['user_id']+"_"+action)
                all_threads.append({"Action": action, "Thread": th})
                th.start()
                print("Thread is not running. Creating a new thread.")
                print(all_threads)
                data={"status":"success","message":"Auto email started , Check your phone for the otp and verify it  "}
                return render_template('home/auto-email.html', message=data)

        except Exception as err:
            data={"status":"fail","message":f"The thread cannot be created due to following error :- {err}"}
            return render_template('home/auto-email.html', message=data)
            
        
    return render_template('home/auto-email.html')


@general_bp.route('/auto-text', methods=['GET', 'POST'])
@login_required
def AUTO_TEXT():
    if request.method=="POST":
        print(request.form)
        global all_threads
        all_threads = [thread for thread in all_threads if thread["Thread"].is_alive()]
        action=request.form['action']
        message= request.form['textToSend']
        csv_data=request.files['csvFile']
        if csv_data:
            df = pd.read_csv(csv_data)
        for t in all_threads:
            if t['Action'] == action and t['Thread'].name==session['user_id']+"_"+action and t['Thread'].is_alive():
                print("Thread is running.")
                print(all_threads)
                data={"status":"success","message":"thread already running  "}
                return render_template('home/auto-text.html', message=data)
            # If no running thread found, create a new one
        # th = threading.Thread(target=auto_text, args=(df['Lead_url'],message,session['user_id']), name=session['user_id']+"_"+action)
        th = threading.Thread(target=selenium_task, args=(), name=session['user_id']+"_"+action)
        all_threads.append({"Action": action, "Thread": th})
        th.start()
        print("Thread is not running. Creating a new thread.")
        print(all_threads)
        data={"status":"success","message":"Auto text started , Check your phone for the otp and verify it  "}
        return render_template('home/auto-text.html', message=data)
    
    return render_template('home/auto-text.html')


@general_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Query the database for the user
        user_data = collection.find_one({'username': username, 'password': password})
        print(user_data)
        if user_data:
            session['user_id'] = str(user_data['_id'])
            session['username'] = user_data['username']

            flash('Login successful!', 'success')
            next_url = request.args.get('next') or url_for('general_bp.index')
            return redirect(next_url)
        else:
            print("dfvk;lhgdk;gehjglhg;ghie;g")
            data='Invalid username or password. Please try again.'
            return render_template('home/sign-in.html',message=data )

    return render_template('home/sign-in.html')

@general_bp.route('/get_user_details',methods=['GET'])
def get_user_details():
    user_id=session['user_id']
    user_id = ObjectId(str(user_id))
    data = collection.find_one({"_id": user_id})
    data.pop("_id")
    return data
    

@general_bp.route('/signup', methods=['GET', 'POST'])
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

@general_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))
