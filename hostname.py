import requests

def get_jira_hostname(username, api_token):
    url = "https://wallah.atlassian.net/rest/api/3/serverInfo"  # Replace <your-jira-instance> with your actual Jira instance

    headers = {
        "Accept": "application/json"
    }

    auth = (username, api_token)  # Replace with your Jira username and API token

    try:
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        data = response.json()
        hostname = data["baseUrl"]
        return hostname
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Usage
jira_username = "forme4005@gmail.com"
api_token = "ATATT3xFfGF0LSPaxm9LmwRa-XvbGbUP5e6Zny1Z6Qn7PVWQDSVVtnlJDxN-Z1hEXjbZTa03MZ-v6uqcYtHG21svxM8BFbpc-qMz6MKo32wNQK2HH9u3YJaHNSr_8JC3fyHyIZX4ZgVG6D4tRMjs2EXkuEUw2gzc6PL14_lS7cevsQquhROF0PY=052268EA"

jira_hostname = get_jira_hostname(jira_username, api_token)
print("Jira Hostname:", jira_hostname)
