import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    # retrieving all the quote <div> HTML element on the page
    quote_elements = soup.find_all('div', class_='result')
    # iterating over the list of quote elements
    # to extract the data of interest and store it
    # in quotes
    for quote_element in quote_elements:
        # extracting the text of the quote
        resto = quote_element.find('span').text
        rue = quote_element.find('div', class_='street-address').text
        ville = quote_element.find('div', class_='locality').text
        num_tel=quote_element.find('div', class_='phones phone primary').text

        restos_NY.append(
            {
                'resto': resto,
                'rue': rue,
                'ville': ville,
                'num_tel' : num_tel

            }
        )

# the url of the home page of the target website
base_url = 'https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New+York%2C+NY'

# defining the User-Agent header to use in the GET request below
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

# parsing the target web page with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

#liste pour stoquer nos données
restos_NY = []

# scraping the home page
scrape_page(soup, restos_NY)

# overture du fichier csv en mode ecriture
csv_file = open('restos_NY', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# cration des champs du fichier csv
writer.writerow(['resto','rue','ville','num'])

# writing each row of the CSV
for quote in restos_NY:
    writer.writerow(quote.values())

# fermeture du fichier csv
csv_file.close()