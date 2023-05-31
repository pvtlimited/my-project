from jira import JIRA
api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"
url = 'https://wallah.atlassian.net/'
user = 'forme4005@gmail.com'
jira = JIRA(url, basic_auth=(user, api_token))

issues = jira.search_issues('')
# Print issue key and summary
for issue in issues:
    data = (issue.key, issue.fields.summary, issue.fields.issuetype)
    issue_key = data[0]
    summary = data[1]
    issue_type_name = data[2].name
    issue_type_id = data[2].id

    # Prepare the transformed data
    transformed_data = [
        (issue_key, summary, issue_type_name, issue_type_id)
    ]

    print(data)
