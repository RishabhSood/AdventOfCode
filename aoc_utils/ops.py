import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

base_url = "https://adventofcode.com"
session_cookie = "53616c7465645f5ff11f53103ffdc003afe495d5c0e17e7fe408aaa9ca11feb1db6dd4681bcce1db0e49c756ecf1afdf2da92bf78161a107ee15ce6eca3687a4"  # Replace <session> with your actual session value

# Set up headers with the session cookie
headers = {
    "Cookie": f"session={session_cookie}"
}

def get_input(year, day, save=False):
    input_url = f"{base_url}/{year}/day/{day}/input"

    response = requests.get(input_url, headers=headers)

    if response.status_code == 200:
        if save:
            with open("input.txt", 'w') as f:
                f.write(response.text)
        return response.text
    else:
        return f"Failed to fetch data: {response.status_code}"
    
def get_problem(year, day, save=False):
    input_url = f"{base_url}/{year}/day/{day}"

    response = requests.get(input_url, headers=headers)
    if response.status_code != 200:
        return f"Failed to fetch data: {response.status_code}"
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the <main> tag
    main_content = soup.find('main')  # Finds the first <main> tag

    if main_content:
        # Get the HTML inside the <main> tag
        main_html = str(main_content)
        mkd = markdownify(main_html)
        if save:
            with open("problem_statement.md", 'w') as f:
                f.write(mkd)

        return mkd
    else:
        return response.text