import requests
import csv
from bs4 import BeautifulSoup

# Make a request to the website
# initial_url = 'https://toscrape.com/'


class Bot():
    def __init__(self, initial_url, file_name):
        self.initial_url = initial_url
        self.file_name = file_name + '.csv'
        self.export_data = []


    def checkStatusCode(self, url):
        response = requests.get(url)
        return response.status_code



    def scrapLinks(self):
        response = requests.get(self.initial_url)
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all of the anchor tags in the page
        links = soup.find_all('a')
        # Returning a list of unique links
        return list(set(links))

    def run(self):
        initial_links = self.scrapLinks()
        for link in initial_links:
            status = self.checkStatusCode(link.get('href'))
            self.export_data.append([link.get('href'), status])


        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.export_data)




# # print("Initial Links: ", initial_links)
# # Extract the href attribute from each link
# for link in initial_links:
#     print("Initial Link: ",link.get('href'))
#     sub_links = scrapLinks(link.get('href'))
#     for link in sub_links:
#         print("Sub Links: ", link.get('href'))