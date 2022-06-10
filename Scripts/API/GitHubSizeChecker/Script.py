import requests


def SizeChecker(username, repository):
    response = requests.get(
        f"https://api.github.com/repos/{username}/{repository}"
    )  # Requesting information about the repository
    if response.status_code == 200:  # The repository exists
        print(f"Success! Repository '{repository}' found.")
        content = response.json()
        size = content["size"]
        print(f"Size of the repository '{repository}': {size} KB.")
    elif response.status_code == 404:
        print("Error 404: Page not found. This could be due to two reasons:")
        print("1. You've entered the wrong details.")
        print("2. The repository you're looking for is a private repository.")


if __name__ == "__main__":
    choice = "y"
    while choice.lower() == "y" or choice.lower() == "yes":
        username = input("Enter a GitHub username: ")
        repository = input("Enter the repository name: ")
        SizeChecker(username, repository)
        choice = input(
            "Do you want to keep searching for more repositories? (y/yes for yes, any other key for no): "
        )
