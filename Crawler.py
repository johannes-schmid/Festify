import requests
# This is needed to search in the html response specific elements
from bs4 import BeautifulSoup

# Creating Crawler Class
class Crawler:
    # Creating object that contains all websites
    websites = {
        'Dekmantel': 'https://www.dekmantelfestival.com/en/tickets/',
        'Sonar': 'https://sonar.es/es/2021/tickets'
    }
    # Elements that need to be tracked
    htmlElements = {
        'Dekmantel': 'tickets',
        'Sonar': 'main-container sm-full-width page_tickets lg-margin-top'
        }
    #Creating run call that crawles websites
    def run(self):
        for website, element in zip(self.websites,self.htmlElements):
            # Sending request to get all page information
            x = requests.get(self.websites[website])
            # Converting it into a readable html page and stripping all un-necessary elements
            x = BeautifulSoup(x.text, 'html.parser').find_all(class_=self.htmlElements[element])
            # Open connection to new file
            f = open(website, 'w')
            # Write text content to file
            f.write(str(x))
            f.close()
