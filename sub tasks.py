from jira import JIRA
from flask import Flask,render_template,request,url_for,session,redirect

api_token="ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
url='https://wallah.atlassian.net/'
user='forme4005@gmail.com'
jira_connection = JIRA(url, basic_auth=(user, api_token))

parent_issue = jira_connection.issue('JUS-18')

project_key = parent_issue.fields.project.key
parent_issue_key = parent_issue.key
print(parent_issue_key)
print(project_key)

# create the subtask
subtask = jira_connection.create_issue(
    project=project_key,
    summary='Sample Subtask Title',
    description='Sample detailed subtask description',
    issuetype={'name': 'Sub-task'},

    parent={'key': parent_issue_key}
)

print(subtask)
"""desc_data = request.form['desc']
summary_subtask = request.form['summary']
priority_data = request.form['priority']
project_name = request.form['project_name']
assignee_id = request.form['assignee']
parent_issue = jira_connection.issue(desc_data)

project_key = parent_issue.fields.project.key
parent_issue_key = parent_issue.key

# create the subtask
subtask = jira_connection.create_issue(
    project=ticket_data,
    summary=summary_subtask,
    description=desc_data,
    issuetype={'name': 'Sub-task'},
    parent={'key': parent_issue_key}, assignee={'id': assignee_id}
)
"""