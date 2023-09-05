import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.cnn.com/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

def get_headlines():
    headline_list = []

    URLscrapp = soup.findAll("div", class_="container__headline container_bulleted-headlines__headline")

    for URLscrapp in URLscrapp:
        headline_text = URLscrapp.span.text
        headline_list.append(headline_text)

    return headline_list

def get_links():
    link_list = []

    URLscrapp = soup.findAll('a', class_='container__link container_bulleted-headlines__link container_bulleted-headlines__left container_bulleted-headlines__light')

    for anchor_element in URLscrapp:
        link = anchor_element.get('href')
        link_list.append("https://www.cnn.com" + link)

    return link_list

def save_to_csv(headlines, links):
    csv_file_name = 'cnn_headlines.csv'

    with open(csv_file_name, 'w', newline='') as csvfile:
        fieldnames = ['Headline', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for headline, link in zip(headlines, links):
            writer.writerow({'Headline': headline, 'Link': link})

    print(f'Headlines and links have been saved to {csv_file_name}')

if __name__ == "__main__":
    headlines = get_headlines()
    links = get_links()
    save_to_csv(headlines, links)




