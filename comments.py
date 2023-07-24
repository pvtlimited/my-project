from datetime import datetime
from jira import JIRA
api_token="ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
url='https://wallah.atlassian.net/'
user='forme4005@gmail.com'
jira_connection = JIRA(url, basic_auth=(user, api_token))

jira_issue = jira_connection.issue("FP-2")
comm=jira_issue.fields.comment.comments
issue_comments = jira_issue.fields.comment.comments
list_for=[]
for comment in comm:
    auther_name=comment.author.displayName
    comment_body=comment.body
    created=comment.created
    date_obj = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
    custom_date_format = "%d-%m-%Y %H:%M:%S"
    formatted_date = date_obj.strftime(custom_date_format)
    print(auther_name)
    print(comment_body)
    transferred_data=(auther_name,comment_body,formatted_date)
    print(transferred_data)
    list_for.append(transferred_data)