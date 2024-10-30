import requests
import os
import json
from constants import GIT_AUTH_TOKEN

# Set up headers for the API request
headers = {
    "Authorization": f'{GIT_AUTH_TOKEN}'
}

# Base URL for GitHub search API
url = "https://api.github.com/search/users?q=location:Zurich+followers:>50"

# Cache file for storing user data
cache_file = "user_cache.json"
response_cache = []

# Load existing data from cache if available
if os.path.exists(cache_file):
    with open(cache_file, 'r') as f:
        response_cache = json.load(f)
    print("From Cache")

# Fetch data from API if cache is empty
if not response_cache:
    print("From API")
    page = 1
    while True:
        curr_url = url + f"&page={page}&per_page=100"
        response = requests.get(curr_url, headers=headers)
        data = response.json()

        print("current url:", curr_url)
        print("Users Fetched:", len(data['items']) if data['items'] else 0)

        response_cache.extend(data.get('items', []))

        if not data.get('items'):
            print("No more Users to fetch!")
            break

        page += 1

    # Save fetched data to cache
    with open(cache_file, 'w') as f:
        json.dump(response_cache, f)

# Output the total number of users fetched
print(f"Total users fetched: {len(response_cache)}")

# if response_cache:
#     print(response_cache[0])  # Print the first user's details for Debugging

# # Uncomment to check current rate limit
# response = requests.get("https://api.github.com/rate_limit", headers=headers)
# print(response.json())
