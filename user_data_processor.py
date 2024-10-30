import pandas as pd
import requests
from github_data_fetcher import get_users, headers

users = get_users()

user_data = []
n = 1
for user in users:
    url = user['url']
    response = requests.get(url, headers=headers)
    user_info = {}
    if response.status_code == 200:
        data = response.json()
        user_info['login'] = data.get('login')
        user_info['name'] = data.get('name')
        user_info['company'] = data.get('company')
        user_info['location'] = data.get('location')
        user_info['email'] = data.get('email')
        user_info['hireable'] = data.get('hireable')
        user_info['bio'] = data.get('bio')
        user_info['public_repos'] = data.get('public_repos')
        user_info['followers'] = data.get('followers')
        user_info['following'] = data.get('following')
        user_info['created_at'] = data.get('created_at')
        print(f"Added user{n}: {user['login']}")
        n += 1
    else:
        print(f"Error Fetching data for user:{user['login']}, Error Code:", response.status_code)
    
    if user_info: user_data.append(user_info)

df = pd.DataFrame(user_data)

def clean_company_names(company): 
    return company.strip().lstrip('@').upper() if pd.notna(company) else company


df['company'] = df['company'].apply(clean_company_names)
df.to_csv('users.csv', index=False)
print("User data saved!")