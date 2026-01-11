import requests
import yaml
import sys

# --- CONFIGURATION ---
GITHUB_USERNAME = "DoodlesEpic"
OUTPUT_FILENAME = "projects.yml"
INCLUDE_FORKS = False  # Set to True if you want to include forked repositories

def get_repos(username):
    """
    Fetches repositories from GitHub API. 
    Handles pagination to ensure we get all repos.
    """
    repos = []
    page = 1
    base_url = f"https://api.github.com/users/{username}/repos"
    
    print(f"Fetching repositories for user: {username}...")
    
    while True:
        params = {
            "type": "owner",
            "sort": "updated",
            "direction": "desc",
            "per_page": 100,
            "page": page
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                break
                
            repos.extend(data)
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            sys.exit(1)
            
    return repos

def format_repo_data(repo):
    """
    Maps GitHub API JSON data to the specific YAML structure required.
    """
    # Create a dictionary with specific key order
    return {
        "name": repo.get("name"),
        "url": repo.get("html_url"),
        "description": repo.get("description"),
        # Mapping snake_case API fields to camelCase YAML fields
        "createdAt": repo.get("created_at"),
        "updatedAt": repo.get("updated_at"),
        "language": repo.get("language"),
        "license": repo.get("license"), # Passes the whole dict or None
        "topics": repo.get("topics", [])
    }

def generate_yaml():
    repos = get_repos(GITHUB_USERNAME)
    processed_projects = []

    for repo in repos:
        # Filter out forks unless configured otherwise
        if not INCLUDE_FORKS and repo.get("fork"):
            continue
            
        # Filter out the profile readme repo (usually same name as username)
        if repo.get("name") == GITHUB_USERNAME:
            continue

        processed_projects.append(format_repo_data(repo))

    print(f"Found {len(processed_projects)} projects. Generating YAML...")

    # Custom Dumper to handle long strings (descriptions) cleanly
    class IndentDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(IndentDumper, self).increase_indent(flow, False)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        # sort_keys=False preserves the order defined in format_repo_data
        yaml.dump(
            processed_projects, 
            f, 
            Dumper=IndentDumper, 
            default_flow_style=False, 
            sort_keys=False, 
            allow_unicode=True
        )

    print(f"Successfully created {OUTPUT_FILENAME}")

if __name__ == "__main__":
    generate_yaml()
