# TDS-IITM-Project1

#### Project overview
The aim of this project was to use GITHUB API to scrape all scrape all users in the city of Zurich with over 50 followers, and their repositories to analyze trends and insights within the collected data. 

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
- '(https://api.github.com/search/users?q=location:Zurich+followers:>50)': to search for the users in zurich with over 50 followers

## Findings

### Interesting Fact
During data analysis, it was surprising to find that some popular repositories had minimal stars, while lesser-known projects sometimes garnered significant attention.

### Recommendation for Developers
Keep repository documentation clear and up-to-date. Projects with descriptive READMEs and well-maintained documentation attract more followers and contributors.
