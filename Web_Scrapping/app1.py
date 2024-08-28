import requests
from bs4 import BeautifulSoup
import re

def scrape_vulnerability_data():
    urls = [
        'https://example-oem.com/security-advisories',
        'https://another-oem.com/vulnerabilities'
    ]
    vulnerabilities = []

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example parsing logic, adjust to actual OEM website structure
            for item in soup.find_all('div', class_='vulnerability'):
                product_name = item.find('h2').text.strip()
                vulnerability = item.find('p', class_='description').text.strip()
                severity = item.find('span', class_='severity').text.strip()
                mitigation = item.find('a', class_='mitigation')['href'].strip()
                published_date = item.find('time')['datetime']

                vulnerabilities.append({
                    'product_name': product_name,
                    'vulnerability': vulnerability,
                    'severity': severity,
                    'mitigation': mitigation,
                    'published_date': published_date
                })
        except requests.exceptions.RequestException as e:
            print(f"Error scraping {url}: {e}")

    return vulnerabilities
