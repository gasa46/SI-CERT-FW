import requests
import re

# Fetch the content from the URL
response = requests.get('https://www.cert.si/misp/urls/last.txt')

# Check if the request was successful
if response.status_code == 200:
    content = response.text
    
    # Use a regular expression to find all URLs
    urls = re.findall(r'https?://[^\s]+', content)
    
    # Print the extracted URLs
    for url in urls:
        print(url)
else:
    print(f"Failed to retrieve content: {response.status_code}")
