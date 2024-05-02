import requests
from bs4 import BeautifulSoup
import re

def find_hidden_pages(url):
    hidden_pages = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', href=True)
    for link in links:
        if link['href'].startswith('/'):
            hidden_pages.append(url + link['href'])
    
    return hidden_pages

def scan_for_password_entries(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    password_entries = []
    forms = soup.find_all('form')

    for form in forms:
        for input_field in form.find_all('input'):
            if input_field.get('type') == 'password':
                password_entries.append(input_field.get('name'))
    
    return password_entries

def main():
    target = input("Enter the URL to scan: ")
    
    hidden_pages = find_hidden_pages(target)
    print(f"Hidden pages found: {hidden_pages}")
    
    for page in hidden_pages:
        passwords = scan_for_password_entries(page)
        if passwords:
            print(f"Password entries found on {page}: {passwords}")
        else:
            print(f"No password entries found on {page}")

if __name__ == "__main__":
    main()
