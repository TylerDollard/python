import requests
from bs4 import BeautifulSoup
import os

def download_file(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(directory, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")

url = 'http://www.textfiles.com/directory.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    for link in links:
        href = link.get('href')
        if href.endswith('.txt'):
            textfile_url = 'http://www.textfiles.com/' + href
            download_file(textfile_url, 'downloaded_textfiles')
else:
    print('Failed to fetch HTML content.')


# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all anchor tags (links) within pre tags
    pre_tags = soup.find_all('pre')
    for pre_tag in pre_tags:
        links = pre_tag.find_all('a')
        # Iterate over the links
        for link in links:
            # Get the href attribute (URL) of the link
            href = link.get('href')
            # Check if the link ends with '.txt'
            if href.endswith('.txt'):
                # Construct the absolute URL
                file_url = 'http://www.textfiles.com/' + href
                # Download the file
                download_file(file_url, 'downloaded_files')
else:
    print('Failed to fetch HTML content.')


# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all anchor tags (links) within pre tags
    pre_tags = soup.find_all('pre')
    for pre_tag in pre_tags:
        links = pre_tag.find_all('a')
        # Iterate over the links
        for link in links:
            # Get the href attribute (URL) of the link
            href = link.get('href')
            # Check if the link ends with '.txt'
            if href.endswith('.txt'):
                # Construct the absolute URL
                file_url = 'http://www.textfiles.com/' + href
                # Download the file
                download_file(file_url, 'downloaded_files')
else:
    print('Failed to fetch HTML content.')


# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all anchor tags (links)
    links = soup.find_all('a')
    # Iterate over the links
    for link in links:
        # Get the href attribute (URL) of the link
        href = link.get('href')
        # Check if the link is a text file
        if href.endswith('.txt'):
            # Download the text file
            file_url = url + href
            file_name = href.split('/')[-1]  # Extract the file name from the URL
            print(f'Downloading {file_name}...')
            # Send a GET request to download the file
            file_response = requests.get(file_url)
            # Check if the request was successful
            if file_response.status_code == 200:
                # Save the file to disk
                with open(file_name, 'wb') as f:
                    f.write(file_response.content)
                print(f'{file_name} downloaded successfully.')
                # Scrape content from the HTML file
                scrape_html_file(file_name)
            else:
                print(f'Failed to download {file_name}.')
else:
    print('Failed to fetch HTML content.')
