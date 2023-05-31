from jira import JIRA
api_token="ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
url='https://wallah.atlassian.net/'
user='forme4005@gmail.com'
jira = JIRA(url, basic_auth=(user, api_token))

issues = jira.search_issues('')
for i in issues:
    key= i.key

# Print issue key and summary
for issue in issues:
    print(issue.key,',',issue.fields.summary,',',issue.fields.issuetype)


'''issue = jira.issue('JUS-24')
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)
print(issue.fields.summary)
commen=issue.fields.comment.comments
for i in commen:
    print(i.body)'''