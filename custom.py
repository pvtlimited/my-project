from jira import JIRA

"""url = 'https://note.atlassian.net'
    user = 'farooqthescout2018@gmail.com'
    api_token = 'ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE'
    jira_connection = JIRA(url, basic_auth=(user, api_token))"""
# Establish connection to Jira
jira_url = 'https://note.atlassian.net'
jira_username = 'farooqthescout2018@gmail.com'
jira_api_token = 'ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE'

jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_api_token))

# Add a comment to an issue
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
new_comment = add_comment(issue_key, 'Husnain Bhai')
print(f"New comment added. Comment ID: {new_comment.id}")


list_wala=[]
issue_comments = read_comments(issue_key)
for comment in issue_comments:
    #print(f"- {comment.body} by {comment.author.displayName}")
    author=comment.author.displayName
    comments_body=comment.body
    transferred_data=(author,comments_body)
    list_wala.append(transferred_data)
print(list_wala)