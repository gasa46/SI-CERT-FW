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
with open('SI-CERT-last1.txt', 'w') as file:
    for url in urls:
        file.write(url + '\n')
print("Extracted URLs have been saved to SI-CERT-last.txt")

try:
    response = requests.get('https://www.cert.si/misp/urls/last.txt', timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching the URL: {e}")
