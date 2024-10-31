import pandas as pd
from github_data_fetcher import get_repos

users_df = pd.read_csv('users.csv')

# Helper function to process boolean and None values
def process_field(value):
    if isinstance(value, bool):
        return str(value).lower() 
    return value if value is not None else "" 


repo_data = []

n = 1
for index, row in users_df.iterrows():
    user_login = row['login']
    print(f'Fetching repos for user{n}: {user_login}')
    user_repos = get_repos(user_login)
    before = len(repo_data)
    for repo in user_repos[:500]:
        repo_info = {
            'login': process_field(user_login),
            'full_name': process_field(repo['full_name']),
            'created_at': process_field(repo['created_at']),
            'stargazers_count': process_field(repo['stargazers_count']),
            'watchers_count': process_field(repo['watchers_count']),
            'language': process_field(repo['language']),
            'has_projects': process_field(repo['has_projects']),
            'has_wiki': process_field(repo['has_wiki']),
            'license_name': process_field(repo['license']['key'] if repo['license'] else '')
        }

        repo_data.append(repo_info)
    
    print(f'Fetched Repos: {len(repo_data) - before}')
    n += 1

print("Fetched Repos for all users!")
print(f"Total repos Fetched: {len(repo_data)}")

repos_df = pd.DataFrame(repo_data)

repos_df.to_csv('repositories.csv', index=False)
print("Repository data saved to repositories.csv!")