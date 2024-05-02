import requests
from bs4 import BeautifulSoup

# Function to scan the website for PHP and JavaScript files
def scan_website(url):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the script tags for JavaScript files
        js_files = soup.find_all('script')
        
        # Find all the links for PHP files
        php_files = [link['href'] for link in soup.find_all('a', href=True) if link['href'].endswith('.php')]
        
        # Print out the JavaScript and PHP files found
        print("JavaScript files:")
        for js_file in js_files:
            print(js_file.get('src'))
        
        print("\nPHP files:")
        for php_file in php_files:
            print(php_file)
    else:
        print("Error scanning website. Status Code:", response.status_code)

# Main script
url = input("Enter a URL to scan: ")
scan_website(url)
