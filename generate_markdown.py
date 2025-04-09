import requests

# Replace 'DibyadyutiDas' with your GitHub username
username = 'DibyadyutiDas'
url = f'https://api.github.com/users/{username}/repos'

# Fetch the repositories
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error fetching repositories: {response.status_code}")
    print(response.json())  # Print the error message from GitHub API
    exit(1)

repos = response.json()

# Start Markdown table
markdown_table = "| Project Name | Description | Repository Link |\n"
markdown_table += "|--------------|-------------|------------------|\n"

# Populate the Markdown table with repository data
for repo in repos:
    name = repo['name']
    description = repo['description'] if repo['description'] else 'No description available'
    link = repo['html_url']
    markdown_table += f"| {name} | {description} | [Link]({link}) |\n"

# Write the Markdown table to README.md
with open('README.md', 'w') as f:
    f.write("# My GitHub Projects\n\n")
    f.write(markdown_table)

print("README.md has been updated.")
