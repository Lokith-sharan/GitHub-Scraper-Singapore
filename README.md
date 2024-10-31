# GitHub-Scraper-Singapore

### Project Overview
* This project scrapes GitHub user data for users in Singapore with over 100 followers using the GitHub API.
* Surprisingly, most users in Singapore with over 100 followers use JavaScript and Python as their primary languages.
* Developers should consider enhancing their GitHub profiles by contributing to popular projects in these languages.

## Files
* `users.csv`: Contains details about GitHub users from Singapore with over 100 followers.
* `repositories.csv`: Contains details about the repositories of these users.

## How Data Was Scraped
1. **Fetching Users**: Used the GitHub API to fetch users in Singapore with more than 100 followers.
2. **Fetching User Details and Repositories**: Retrieved detailed information and repositories for each user.
3. **Data Cleaning and Formatting**: Cleaned company names, ensured proper formatting, and saved data to CSV files.

## Interesting Finding
* The analysis showed that JavaScript and Python are the dominant languages among top developers in Singapore, highlighting their popularity and demand in the region.

## Recommendation for Developers
* Enhance their GitHub presence by contributing to trending JavaScript and Python projects, as they are highly popular among top developers in Singapore.

## Scripts Used
* `main.py`: Python script to scrape data from GitHub and create the CSV files.

