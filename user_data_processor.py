import pandas as pd
import requests
from github_data_fetcher import get_users, headers

users = get_users()

# Helper function to process boolean and None values
def process_field(value):
    if isinstance(value, bool):
        return str(value).lower() 
    return value if value is not None else "" 

user_data = []
n = 1
for user in users:
    url = user['url']
    response = requests.get(url, headers=headers)
    user_info = {}
    if response.status_code == 200:
        data = response.json()
        user_info['login'] = process_field(data.get('login'))
        user_info['name'] = process_field(data.get('name'))
        user_info['company'] = process_field(data.get('company'))
        user_info['location'] = process_field(data.get('location'))
        user_info['email'] = process_field(data.get('email'))
        user_info['hireable'] = process_field(data.get('hireable'))
        user_info['bio'] = process_field(data.get('bio'))
        user_info['public_repos'] = process_field(data.get('public_repos'))
        user_info['followers'] = process_field(data.get('followers'))
        user_info['following'] = process_field(data.get('following'))
        user_info['created_at'] = process_field(data.get('created_at'))
        print(f"Added user{n}: {user['login']}")
        n += 1
    else:
        print(f"Error Fetching data for user:{user['login']}, Error Code:", response.status_code)
    
    if user_info: user_data.append(user_info)

df = pd.DataFrame(user_data)

df['company'] = df['company'].apply(lambda x: x.strip().lstrip('@').upper() if isinstance(x, str) else "")

df.to_csv('users.csv', index=False)
print("User data saved!")