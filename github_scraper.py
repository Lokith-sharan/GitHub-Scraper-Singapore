import requests
import csv
import os

GITHUB_TOKEN = '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'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}
USER_SEARCH_URL = 'https://api.github.com/search/users?q=location:Singapore+followers:>100&per_page=100'
REPOS_URL_TEMPLATE = 'https://api.github.com/users/{username}/repos?per_page=500'

def fetch_users():
    response = requests.get(USER_SEARCH_URL, headers=HEADERS)
    response.raise_for_status()
    return response.json()['items']

def fetch_user_details(username):
    user_url = f'https://api.github.com/users/{username}'
    response = requests.get(user_url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def fetch_user_repos(username):
    repos_url = REPOS_URL_TEMPLATE.format(username=username)
    response = requests.get(repos_url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def clean_company_name(company):
    if company:
        company = company.strip()
        if company.startswith('@'):
            company = company[1:]
        return company.upper()
    return ''

def write_users_csv(users):
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at'])
        for user in users:
            writer.writerow([
                user['login'],
                user.get('name', ''),
                clean_company_name(user.get('company', '')),
                user.get('location', ''),
                user.get('email', ''),
                user.get('hireable', 'false'),
                user.get('bio', ''),
                user['public_repos'],
                user['followers'],
                user['following'],
                user['created_at']
            ])

def write_repositories_csv(repositories):
    with open('repositories.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name'])
        for repo in repositories:
            writer.writerow([
                repo['owner']['login'],
                repo['full_name'],
                repo['created_at'],
                repo['stargazers_count'],
                repo['watchers_count'],
                repo.get('language', ''),
                str(repo['has_projects']).lower(),
                str(repo['has_wiki']).lower(),
                repo['license']['name'] if repo['license'] else ''
            ])

def main():
    users = fetch_users()
    user_details = [fetch_user_details(user['login']) for user in users]
    repositories = []
    for user in user_details:
        user_repos = fetch_user_repos(user['login'])
        repositories.extend(user_repos)

    write_users_csv(user_details)
    write_repositories_csv(repositories)
    print("CSV files have been created successfully!")

if __name__ == "__main__":
    main()




















































