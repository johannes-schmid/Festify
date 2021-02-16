import requests
# This is needed to search in the html response specific elements
from bs4 import BeautifulSoup
# Date time module to track stamp current time
import datetime
import pandas as pd

# Creating Crawler Class
class Crawler:
    events = ['Dekmantel', 'Sonar']
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
        # Reading csv file
        df = pd.read_csv('data/changes.csv')
        df.set_index('Event', inplace=True)
        for event in self.events:
            eventWebsite = self.websites[event]
            eventElement = self.htmlElements[event]
            # Sending request to get all page information
            x = requests.get(eventWebsite)
            # Converting it into a readable html page and stripping all un-necessary elements
            x = str(BeautifulSoup(x.text, 'html.parser').find(class_=eventElement))
            # Open connection to new file
            f = open('data/' + event + '.html')
            fileContent = f.read()
            f.close()
            if x == fileContent:
                print('There are no changes my friends!')
            else:
                f = open('data/' + event + '.html', 'w')
                f.write(x)
                f.close()
                # Changing cell with last changed date
                if event in df.index:
                    df.loc[event, 'last change'] = str(datetime.datetime.now())
                else:
                    df = df.append([event], str(datetime.datetime.now()))

            df.to_csv('data/changes.csv')
