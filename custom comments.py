from jira import JIRA
url = 'https://note.atlassian.net'
user = 'farooqthescout2018@gmail.com'
api_token = 'ATATT3xFfGF00EtiKece8swJev6Nf2c2hEzb3mQP_SaCxoE5qjRSKYKx99g4m_Fg1qz6NxDnheW1jDeYEm7MEhq-5-MHirMqmr2KWNDFk7GXslH9rqEpGUUtmFxTdEiP4Tip_kkX0Bn3Kf44DirrL8mmnA_ISzjGGwxHtiNc6TSsaCt649TyN4o=5715ACBE'
jira= JIRA(url, basic_auth=(user, api_token))
comment_to_edit = jira.add_comment('JUS-1', 'Change this content later')
comment_to_edit.update(body='New Content.')