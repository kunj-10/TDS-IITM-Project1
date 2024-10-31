# TDS-IITM-Project1

#### Project overview
The aim of this project was to use the GitHub API to scrape all users in the city of Zurich with over 50 followers and their repositories. This data was analyzed to identify trends and insights. 

***Before use***: Add your personal github auth token to 'constants.py' in variable 'GIT_AUTH_TOKEN'

## Steps Followed
1. Scraping User Data
    - The user data is fetched using the get_user function in github_data_fetcher.py, which retrieves user information from the GitHub API and stores it in **users.csv**.

2. Scraping Repository Data
    - Repository data for each user is fetched using the get_repos function in github_data_fetcher.py, collecting details like repository name, creation date, stars, and language, and saving them in **repositories.csv**.

3. Data Processing
    - Boolean values are saved as 'true' or 'false'.
    - Null values are represented as empty strings.
    - Company names are cleaned by removing leading @ symbols and converting to uppercase.

4. Answering the Questions
    - Using pandas to load **users.csv** and **repositories.csv** 
    - Employing various pandas and sklearn functionalities, such as *LinearRegression* from *sklearn.linear_model*, to analyze the data and answer specific research questions.

#### Endpoints used:
The following GitHub API endpoints were used for data retrieval:
- 'https://api.github.com/search/users?q=location:Zurich+followers:>50': to search for the users in zurich with over 50 followers
- 'https://api.github.com/users/{USERNAME}': to get the details of individual users
- 'https://api.github.com/users/{user_login}/repos?per_page=100': to get the repositories associated with a user

## Findings

### Interesting Fact
- During data analysis, it was surprising to find that the programming language **BitBake** had the highest average number of stars among repositories, suggesting a niche interest that may not correlate with the popularity of the repositories themselves.
-  Also it was interesting to find how Python is the single largest language used in Zurich and how in more recent repositories Javascript has grown to become the second largest language used

### Recommendations for Developers
1. **Focus on Public Repositories**: To increase follower count, developers should consider maintaining and promoting their public repositories, as more repositories are positively associated with higher follower counts.
2. **Enhance Project and Wiki Features**: Enabling project and wiki features may attract more followers, given the observed correlation.
3. **Optimize Bio Content**: Developers should craft informative bios, as word count in bios appears to significantly influence follower growth. Clear and engaging bios may lead to increased interest in their projects.
4. **Keep Documentation Clear and Up-to-Date**: Projects with descriptive READMEs and well-maintained documentation attract more followers and contributors.
