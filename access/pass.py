import requests
from bs4 import BeautifulSoup

# Prompt the user to enter a domain name
domain_name = input("Please enter the domain name: ")
url = "http://" + domain_name

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find all password entry fields in the website
password_fields = soup.find_all("input", {"type": "password"})

if len(password_fields) > 0:
    print("Password entry fields found on the website.")
else:
    print("No password entry fields found on the website.")
