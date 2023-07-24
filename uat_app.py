import time
from jira import JIRA, JIRAError

import requests
from flask import Flask,render_template,request,url_for,session,redirect,got_request_exception
#from flask_mysqldb import MySQL
from datetime import *
import time as t
import mysql.connector
from jira import JIRA, JIRAError
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="passwordis@2018",
            database="farooq",
            consume_results=True
)
app = Flask(__name__)
app.secret_key='JustMe'
myhome="HOME PAGE!!!!!!!!!!!!!!!!!!!!!!!"


@app.route("/")		#http://127.0.0.1:5000
def login_form():
    return render_template("login.html")
@app.route("/login_create", methods = ['POST','GET'])
def login_create():
    msg= ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #email = request.form['email']
        cursor = mydb.cursor()
        '''sql = "INSERT INTO authen (username,password,email) VALUES (%s, %s, %s)"
        val = (username, password, email)
        cursor.execute(sql, val)
        mydb.commit()'''
        cursor.execute('select * from users where username = %s and password = %s', (username,password))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account[1]
            session['username'] = account[2]
            return render_template("index.html",username=session['username'])
        else:
            msg = "Please Try Again Buggy, Your Username or Password is Invalid or try to register the new account from Create Account Option "
    return render_template("login.html",msg=msg)

@app.route("/register")
def create():
    return render_template('login_register.html')
@app.route("/register_create",methods=['POST','GET'])
def create_():
        msg= ''
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            cursor = mydb.cursor()
            #sql = "INSERT INTO authen (username,password, email) VALUES (%s, %s, %s)"

            sql="SELECT * FROM users WHERE username=%s"
            val=(str(username),)
            cursor.execute(sql,val)
            account = cursor.fetchone()
            print(account)
            if account:
                msg = "Username already registered!!!"
                return render_template('login.html',msg=msg)
            else:
                sql="INSERT INTO users(username,password,email) VALUES (%s, %s, %s)"
                val = (str(username), str(password), str(email),)
                cursor.execute(sql,val)
                mydb.commit()
                cursor = mydb.cursor()
        elif request.method=="POST":
            msg ="Please enter the details !!!!"
        return render_template('login.html')






'''@app.route("/login_create", methods = ['POST','GET'])
def login_create():
    msg=''
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']

    #sql = "INSERT INTO authen (username,password) VALUES (%s, %s)"
    #	val = (username, password)

        mycursor = mydb.cursor()
        #mycursor.execute(sql, val)
        mycursor.execute('select * from authen where username= %s and password=%s',(username,password))
        account=mycursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account[username]
            return render_template("index.html", username=session['username'])
        else:
            msg='You are not authenticated'

        return render_template("login.html")'''

@app.route("/home")		#http://127.0.0.1:5000
def get_home():
    if 'loggedin' in session:
        return render_template("index.html",username=session['username'])
    return redirect(url_for('login_form'))
#HURRY UP
@app.route("/trainer")		#http://127.0.0.1:5000/contact
def trainer():
    if 'loggedin' in session:
        return render_template("trainer_form.html",username=session['username'])
    return redirect(url_for('login_form'))


@app.route("/trainer_create",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def trainer_create():
    if 'loggedin' in session:
        if request.method == "POST":
            fname_data= request.form['fname']
            lname_data = request.form['lname']
            design_data = request.form['design']
            course_data = request.form['course']
            cdate= date.today()
            sql = "INSERT INTO trainer_details (fname,lname,design,course,datetime) VALUES (%s, %s, %s, %s, %s)"
            val = (fname_data,lname_data,design_data,course_data,cdate)
            #connection
            mycursor=mydb.cursor()
            #execute sql query
            mycursor.execute(sql, val)

            mydb.commit()
            #cursor
            #commit
            #mysql.connection.commit()
            #close
            #cursor.close()
            return render_template('trainer_form.html',username=session['username'])
        return redirect(url_for('login_form'))
#HURRY UP
@app.route("/trainer_details",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def trainer_details():
    if 'loggedin' in session:
        mycursor=mydb.cursor(buffered=True)
        sql="SELECT * FROM trainer_details"
        mycursor.execute(sql)
        row=mycursor.fetchall()
        print(row)
        return render_template('trainer_report.html', output_data=row,username=session['username'])
    return redirect(url_for('login_form'))
'''@app.route("/trainer_filter",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def trainer_filter():
        if request.method == "POST":
            course_search= request.form['course']
            cursor = mydb.cursor()
            if course_search == "All":
                sql = "select * from trainer_details"
                cursor.execute(sql)
                row = cursor.fetchall()'''
#		return redirect(url_for('login_form'))




@app.route("/trainer_filter",methods=['POST','GET'])
def trainer_filter():
    if request.method=="POST":
        course_search=request.form['course']
        mycursor = mydb.cursor()
        if course_search == "All":
            sql="select * from trainer_details"
            mycursor.execute(sql)
            row=mycursor.fetchall()
            return render_template('trainer_report.html',output_data=row)
        else:
            sql = "select * from trainer_details where course=" + course_search
            mycursor.execute(sql)
            row = mycursor.fetchall()
            return render_template('trainer_report.html',output_data=row)



@app.route("/jira")  # http://127.0.0.1:5000/contact
def jira():
    #if 'loggedin' == session:
        return render_template("jira_flask.html",username=session['username'])
    #return redirect(url_for('login_form'))


@app.route("/jira_create", methods=['POST', 'GET'])  # http://127.0.0.1:5000/contact
def jira_create():
    if 'loggedin' in session:
        if request.method == "POST":
            project_data = request.form["project"]
            issuetype_data = request.form['issuetype']
            reporter_data = request.form['reporter']
            desc_data = request.form['desc']
            summary_data = request.form['summary']
            priority_data = request.form['priority']
            assignee_id=request.form['assignee']
            url = 'https://wallah.atlassian.net'
            user = 'forme4005@gmail.com'
            api_token = 'ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA'
            jira = JIRA(url, basic_auth=(user, api_token))
            issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                      description=desc_data, reporter={'id': reporter_data},
                                      priority={'name': priority_data},assignee={'id': assignee_id})
            print(issue)
            return render_template("jira_flask.html",username=session['username'])

        return redirect(url_for('login_form'))

@app.route("/jira_1")  # http://127.0.0.1:5000/contact
def jira_1():
    #if 'loggedin' == session:
        return render_template("jira_flask_1.html",username=session['username'])
    #return redirect(url_for('login_form'))


@app.route("/jira_create_1", methods=['POST', 'GET'])  # http://127.0.0.1:5000/contact
def jira_create_1():
    if 'loggedin' in session:
        if request.method == "POST":
            project_data = request.form["project"]
            issuetype_data = request.form['issuetype']
            reporter_data = request.form['reporter']
            desc_data = request.form['desc']
            summary_data = request.form['summary']
            priority_data = request.form['priority']
            assignee_id = request.form['assignee']
            url = 'https://note.atlassian.net'
            user = 'forme4005@gmail.com'
            api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
            jira = JIRA(url, basic_auth=(user, api_token))
            issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                      description=desc_data, reporter={'id': reporter_data},
                                      priority={'name': priority_data},assignee={'id': assignee_id})
            print(issue)
            return render_template("jira_flask_1.html",username=session['username'])

        return redirect(url_for('login_form'))


@app.route("/jira_2")  # http://127.0.0.1:5000/contact
def jira_2():
    # if 'loggedin' == session:
    return render_template("jira_flask_2.html", username=session['username'])


# return redirect(url_for('login_form'))


@app.route("/jira_create_2", methods=['POST', 'GET'])  # http://127.0.0.1:5000/contact
def jira_create_2():
    if 'loggedin' in session:
        if request.method == "POST":
            project_data = request.form["project"]
            issuetype_data = request.form['issuetype']
            reporter_data = request.form['reporter']
            desc_data = request.form['desc']
            summary_data = request.form['summary']
            priority_data = request.form['priority']
            project_name=request.form['project_name']
            assignee_id = request.form['assignee']
            if project_name == "wallah":
                url = 'https://wallah.atlassian.net'
                user = 'forme4005@gmail.com'
                api_token = 'ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA'
                jira = JIRA(url, basic_auth=(user, api_token))
                if project_data == "FP":
                    issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                              description=desc_data, reporter={'id': reporter_data},assignee={'id': assignee_id})
                else:
                    issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                              description=desc_data, reporter={'id': reporter_data},
                                              priority={'name': priority_data},assignee={'id': assignee_id})

                print(issue)
            elif project_name == "note":
                url = 'https://note.atlassian.net'
                user = 'forme4005@gmail.com'
                api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
                jira = JIRA(url, basic_auth=(user, api_token))
                issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                          description=desc_data, reporter={'id': reporter_data},
                                          priority={'name': priority_data},assignee={'id': assignee_id})
            elif project_name == "All":
                url = 'https://wallah.atlassian.net'
                user = 'forme4005@gmail.com'
                api_token = 'ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA'
                jira = JIRA(url, basic_auth=(user, api_token))
                if project_data == "FP":
                    issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                              description=desc_data, reporter={'id': reporter_data},assignee={'id': assignee_id})
                else:
                    issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                              description=desc_data, reporter={'id': reporter_data},
                                              priority={'name': priority_data},assignee={'id': assignee_id})
                url = 'https://note.atlassian.net'
                user = 'forme4005@gmail.com'

                api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
                jira = JIRA(url, basic_auth=(user, api_token))
                issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                          description=desc_data, reporter={'id': reporter_data},
                                          priority={'name': priority_data},assignee={'id': assignee_id})

            """url = 'https://note.atlassian.net'
            user = 'forme4005@gmail.com'
            api_token = 'ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE'
            jira = JIRA(url, basic_auth=(user, api_token))
            issue = jira.create_issue(project=project_data, summary=summary_data, issuetype=issuetype_data,
                                      description=desc_data, reporter={'id': reporter_data},
                                      priority={'name': priority_data})"""
            print(issue)
            return render_template("jira_flask_2.html", username=session['username'])
        return redirect(url_for('login_form'))


@app.route("/jira_details",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def jira_details():
    if 'loggedin' in session:
        """api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
        url = 'https://wallah.atlassian.net/'
        user = 'forme4005@gmail.com'
        jira = JIRA(url, basic_auth=(user, api_token))
        issues = jira.search_issues('')"""
        cat = []
        # create the subtask
        if request.method == "POST":
            which_form = request.form['which']
            if which_form == "wallah":
                api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
                url = 'https://wallah.atlassian.net/'
                user = 'forme4005@gmail.com'
                jira = JIRA(url, basic_auth=(user, api_token))
                issues = jira.search_issues('')
                for issue in issues:
                    data=(issue.key, issue.fields.summary, issue.fields.issuetype,issue.fields.created, issue.fields.priority,issue.fields.assignee,issue.fields.reporter)
                    issue_key = data[0]
                    summary = data[1]
                    issue_type_name = data[2]
                    created=data[3]
                    priority=data[4]
                    assignee=data[5]
                    reporter_name=data[6]
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%m-%Y %H:%M:%S"
                    formatted_date = date_obj.strftime(custom_date_format)
                    # Prepare the transformed data
                    transformed_data = (issue_key, summary, issue_type_name,formatted_date,priority,assignee,reporter_name)

                    cat.append(transformed_data)
                    print(transformed_data)

                    desc_data = request.form['desc']
                    ticket_data = request.form['tick_number']
                    summary_subtask = request.form['summary']
                    account = request.form['account']
                    which_form = request.form['which']
                    parent_issue = jira.issue(ticket_data)
                    ticket_data = ticket_data.replace(" ", "")
                    project_key = parent_issue.fields.project.key
                    parent_issue_key = parent_issue.key

                    print(parent_issue_key)
                    print(project_key)
                    if account == "wallah":
                        api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
                        url = 'https://wallah.atlassian.net/'
                        user = 'forme4005@gmail.com'
                        jira = JIRA(url, basic_auth=(user, api_token))
                        subtask = jira.create_issue(
                            project=project_key,
                            summary=summary_subtask,
                            description=desc_data,
                            issuetype={'name': 'Sub-task'},
                            parent={'key': ticket_data}
                        )
                        print(subtask)
                    elif account == "note":
                        url = 'https://note.atlassian.net'
                        user = 'forme4005@gmail.com'
                        api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
                        jira = JIRA(url, basic_auth=(user, api_token))
                        subtask = jira.create_issue(
                            project=project_key,
                            summary=summary_subtask,
                            description=desc_data,
                            issuetype={'name': 'Sub-task'},
                            parent={'key': ticket_data}
                        )
                        print(subtask)
                    elif account == "all":
                        api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
                        url = 'https://wallah.atlassian.net/'
                        user = 'forme4005@gmail.com'
                        jira = JIRA(url, basic_auth=(user, api_token))
                        subtask = jira.create_issue(
                            project=project_key,
                            summary=summary_subtask,
                            description=desc_data,
                            issuetype={'name': 'Sub-task'},
                            parent={'key': ticket_data}
                        )
                        url = 'https://note.atlassian.net'
                        user = 'forme4005@gmail.com'
                        api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
                        jira = JIRA(url, basic_auth=(user, api_token))
                        subtask = jira.create_issue(
                            project=project_key,
                            summary=summary_subtask,
                            description=desc_data,
                            issuetype={'name': 'Sub-task'},
                            parent={'key': ticket_data}
                        )
                        print(subtask)

            elif which_form == "note":
                url = 'https://note.atlassian.net'
                user = 'forme4005@gmail.com'
                api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
                jira = JIRA(url, basic_auth=(user, api_token))
                issues = jira.search_issues('')
                for issue in issues:
                    data = (issue.key, issue.fields.summary, issue.fields.issuetype, issue.fields.created,
                            issue.fields.priority, issue.fields.assignee, issue.fields.reporter)
                    issue_key = data[0]
                    summary = data[1]
                    issue_type_name = data[2]
                    created = data[3]
                    priority = data[4]
                    assignee = data[5]
                    reporter_name = data[6]
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%m-%Y %H:%M:%S"
                    formatted_date = date_obj.strftime(custom_date_format)
                    # Prepare the transformed data
                    transformed_data = (
                    issue_key, summary, issue_type_name, formatted_date, priority, assignee, reporter_name)

                    cat.append(transformed_data)
                    print(transformed_data)

            elif which_form == "All":
                api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
                url = 'https://wallah.atlassian.net/'
                user = 'forme4005@gmail.com'
                jira = JIRA(url, basic_auth=(user, api_token))
                issues = jira.search_issues('')
                for issue in issues:
                    data = (issue.key, issue.fields.summary, issue.fields.issuetype, issue.fields.created,
                            issue.fields.priority, issue.fields.assignee, issue.fields.reporter)
                    issue_key = data[0]
                    summary = data[1]
                    issue_type_name = data[2]
                    created = data[3]
                    priority = data[4]
                    assignee = data[5]
                    reporter_name = data[6]
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%m-%Y %H:%M:%S"
                    formatted_date = date_obj.strftime(custom_date_format)
                    # Prepare the transformed data
                    transformed_data = (
                    issue_key, summary, issue_type_name, formatted_date, priority, assignee, reporter_name)

                    cat.append(transformed_data)
                    print(transformed_data)
                url = 'https://note.atlassian.net'
                user = 'forme4005@gmail.com'
                api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
                jira = JIRA(url, basic_auth=(user, api_token))
                issues = jira.search_issues('')
                for issue in issues:
                    data = (issue.key, issue.fields.summary, issue.fields.issuetype, issue.fields.created,
                            issue.fields.priority, issue.fields.assignee, issue.fields.reporter)
                    issue_key = data[0]
                    summary = data[1]
                    issue_type_name = data[2]
                    created = data[3]
                    priority = data[4]
                    assignee = data[5]
                    reporter_name = data[6]
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%m-%Y %H:%M:%S"
                    formatted_date = date_obj.strftime(custom_date_format)
                    # Prepare the transformed data
                    transformed_data = (
                        issue_key, summary, issue_type_name, formatted_date, priority, assignee, reporter_name)
                    cat.append(transformed_data)

        return render_template('trainer_report_jira.html', output_data=cat,username=session['username'] )
    return redirect(url_for('login_form'))

@app.route("/comments",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def comments():
    if 'loggedin' in session:
        list_for = []
        try:
            if request.method == "POST":
                project_number=request.form['project_name']
                url = 'https://note.atlassian.net'
                user = 'forme4005@gmail.com'
                api_token = 'ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D'
    
                jira_connection = JIRA(url, basic_auth=(user, api_token))

                jira_issue = jira_connection.issue(project_number)
                comm = jira_issue.fields.comment.comments
                issue_comments = jira_issue.fields.comment.comments
                list_for = []
                for comment in comm:
                    auther_name = comment.author.displayName
                    comment_body = comment.body
                    created = comment.created
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%B-%Y"
                    formatted_date = date_obj.strftime(custom_date_format)
                    print(auther_name)
                    print(comment_body)
                    transferred_data = (auther_name, comment_body, formatted_date)
                    print(transferred_data)
                    list_for.append(transferred_data)
        except JIRAError as e:
            error_message = e.text
            error_message = "JIRAError: ", error_message
            list_for.append(error_message)
        return render_template('comments.html',output_data=list_for ,username=session['username'])
    return redirect(url_for('login_form'))


@app.route("/comments_1",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def comments_1():
    if 'loggedin' in session:
        list_for=[]

        try:
            if request.method == "POST":
                project_number=request.form['project_name']
                api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
                url = 'https://wallah.atlassian.net/'
                user = 'forme4005@gmail.com'
                jira_connection = JIRA(url, basic_auth=(user, api_token))
                jira_issue = jira_connection.issue(project_number)
                comm = jira_issue.fields.comment.comments
                issue_comments = jira_issue.fields.comment.comments
                list_for = []
                for comment in comm:
                    auther_name = comment.author.displayName
                    comment_body = comment.body
                    created = comment.created
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%B-%Y"
                    formatted_date = date_obj.strftime(custom_date_format)
                    print(auther_name)
                    print(comment_body)
                    transferred_data = (auther_name, comment_body, formatted_date)
                    print(transferred_data)
                    list_for.append(transferred_data)
                if request.method == "POST":
                    ticket_number = request.form['comment_add']
                    issue = jira_connection.issue(project_number)
                    new_comment= jira_connection.add_comment(issue, ticket_number)
        except JIRAError as e:
            # Handle the JIRAError exception
            error_message = e.text
            error_message="JIRAError: ",error_message
            list_for.append(error_message)
        return render_template('comments_1.html',output_data=list_for ,username=session['username'])
    return redirect(url_for('login_form'))


@app.route("/subtask",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def subtask():
    if 'loggedin' in session:
        api_token = "ATATT3xFfGF0vWkYYG1J0jnHxFIYoNHX-S1Jv61Aw9oxaDxzYuHuYpwlvtLMS-AO-2MoDICH8Uyn4aFXY0l1DfRQQMHcyLbvGIEEzIw323hQxgws56xU6p6Nx9rnCxlcHVzv_2vO_QW4gGbT8pDcgz5c1z7G2q5Dv29boOfnAuwIWS9sxEZitFo=0828148D"
        url = 'https://note.atlassian.net/'
        user = 'forme4005@gmail.com'
        if request.method == "POST":
            jira_connection = JIRA(url, basic_auth=(user, api_token))
            ticket_data = request.form['ticket']
            desc_data = request.form['desc']
            summary_data = request.form['summary']
            assignee_id = request.form['assignee']
            priority_data = request.form['priority']
            parent_issue = jira_connection.issue(ticket_data)
            project_key = parent_issue.fields.project.key
            parent_issue_key = parent_issue.key
            # create the subtask
            subtask = jira_connection.create_issue(
                project=project_key,
                summary=summary_data,
                description=desc_data,
                issuetype={'name': 'Sub-task'},
                parent={'key': parent_issue_key}, priority={'name': priority_data}, assignee={'id': assignee_id}
            )

        return render_template('subtask.html',  username=session['username'])
    return redirect(url_for('login_form'))

'''

@app.route("/comments_1",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def comments_1():
    if 'loggedin' in session:
        list_for=[]
        url = 'https://note.atlassian.net'
        user = 'farooqthescout2018@gmail.com'
        api_token = 'ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE'
        jira_connection = JIRA(url, basic_auth=(user, api_token))
        """if request.method == "POST":
            project_number = request.form['project_name']
            def add_comment(issue_key, comment_body):
                issue = jira.issue(issue_key)
                new_comment = jira.add_comment(issue, comment_body)
                return new_comment

            # Read comments of an issue
            def read_comments(issue_key):
                issue = jira.issue(issue_key)
                comments = issue.fields.comment.comments
                return comments

            # Usage example
            issue_key = 'JUS-1'
            new_comment = add_comment(issue_key, 'This is a test comment.')
            print(f"New comment added. Comment ID: {new_comment.id}")

            issue_comments = read_comments(issue_key)
            print("Comments:")
            for comment in issue_comments:
                print(f"- {comment.body} by {comment.author.displayName}")"""
        try:
            if request.method == "POST":
                project_number = request.form['project_name']
                jira_issue = jira_connection.issue(project_number)
                comm = jira_issue.fields.comment.comments
                issue_comments = jira_issue.fields.comment.comments
                list_for = []
                def read_comments(issue_number):
                    issue = jira.issue(issue_number)
                    comments = issue.fields.comment.comments
                    return comments
                project_number = request.form['project_name']
                for comment in issue_comments:
                    # print(f"- {comment.body} by {comment.author.displayName}")
                    author = comment.author.displayName
                    comments_body = comment.body
                    transferred_data = (author, comments_body)
                    list_for.append(transferred_data)
                issue_comment=read_comments(project_number)

                """for comment in comm:
                    auther_name = comment.author.displayName
                    comment_body = comment.body
                    created = comment.created
                    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
                    custom_date_format = "%d-%B-%Y"
                    formatted_date = date_obj.strftime(custom_date_format)
                    print(auther_name)
                    print(comment_body)
                    transferred_data = (auther_name, comment_body, formatted_date)
                    print(transferred_data)
                    list_for.append(transferred_data)
                    if request.method == "POST":
                        name_for_add = request.form['project_name']
                        ticket_number = request.form['tick_number']
                        issue = jira.issue(name_for_add)
                        new_comment = jira.add_comment(issue, ticket_number)"""

        except JIRAError as e:
            # Handle the JIRAError exception
            error_message = e.text
            error_message="JIRAError: ",error_message
            list_for.append(error_message)
        return render_template('comments_1.html',output_data=list_for ,username=session['username'])
    return redirect(url_for('login_form'))'''


'''@app.route("/register")
def create():
    return render_template('register.html')'''

#Register
#Register
#Register
#Register
#Register
#Register
#Register
#Register
#Register
#Register

#Register
#Register
#Register
#Register
#Register
#Register
#Register
#Register
#Register
#Register
'''@app.route("/register",methods=['POST','GET'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form["password"]
        email_data=request.form["email"]
        cursor = mydb.cursor()
        sql="INSERT INTO authen (username,password,email) VALUES (%s, %s, %s)"
        val=(username, password, email_data)
        cursor.execute(sql,val)
        #mydb.commit()
    return redirect(url_for(get_home))'''



#		return redirect(url_for('login_form'))
@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for('login_form'))
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="1113")

#(%s,%s,%s,%s,%s)
#{{ url_for('login_create')}}
#{{url_for('create_account')}}