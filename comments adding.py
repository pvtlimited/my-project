import requests
""" url = 'https://note.atlassian.net'
            user = 'farooqthescout2018@gmail.com'
            api_token = 'ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE'
            """
def add_comment_to_issue(issue_key, comment_body, username, api_token):
    url = f"https://note.atlassian.net/rest/api/3/issue/{issue_key}/comment"  # Replace <your-jira-instance> with your actual Jira instance

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    auth = (username, api_token)  # Replace with your Jira username and API token

    data = {
        "body": comment_body
    }

    try:
        response = requests.post(url, headers=headers, json=data, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Usage
jira_username = 'farooqthescout2018@gmail.com'
jira_api_token = "ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE"
issue_key = "JUS-1"
comment_body = "This is a test comment."  # Replace with the desired comment body

response = add_comment_to_issue(issue_key, comment_body, jira_username, jira_api_token)
if response:
    comment_id = response["id"]
    print(f"Comment added successfully. Comment ID: {comment_id}")
else:
    print("Failed to add comment.")
