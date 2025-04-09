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
markdown_table = "\n\n| Project Name | Description | Repository Link |\n"
markdown_table += "|--------------|-------------|------------------|\n"

# Filter and populate the Markdown table with project data
for repo in repos:
    name = repo['name']
    description = repo['description'] if repo['description'] else 'No description available'
    
    # Filter condition: Only include repositories that contain "project" in their name
    if 'project' in name.lower():  # Change this condition as needed
        link = repo['html_url']
        markdown_table += f"| {name} | {description} | [Link]({link}) |\n"

# Read the existing README.md content
try:
    with open('README.md', 'r') as f:
        existing_content = f.read()
except FileNotFoundError:
    existing_content = ""  # If the file doesn't exist, start with an empty string

# Write the existing content and append the Markdown table
with open('README.md', 'w') as f:
    f.write(existing_content)  # Write the existing content
    f.write("# My GitHub Projects\n")  # Add the header if it's not already there
    f.write(markdown_table)  # Append the new table

print("README.md has been updated.")
