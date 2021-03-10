import requests
# This is needed to search in the html response specific elements
from bs4 import BeautifulSoup
# Date time module to track stamp current time
import datetime
import pandas as pd

from src.services.Notifier import Notifier


# Creating Crawler Class
class Crawler:

    events = ['Dekmantel', 'Sonar']

    # Creating object that contains all websites
    websites = {
        'Dekmantel': 'https://www.dekmantelfestival.com/en/tickets/',
        'Sonar': 'https://sonar.es/es/2021/tickets'
    }

    # Elements that need to be tracked
    htmlElementClasses = {
        'Dekmantel': 'tickets',
        'Sonar': 'main-container sm-full-width page_tickets lg-margin-top'
    }

    # Creating run call that crawls websites
    def run(self):
        # Reading csv file
        df = pd.read_csv('../data/changes.csv', index_col='Event')
        # Creating notifier
        notifier = Notifier()

        for event in self.events:

            website = self.websites[event]
            classname = self.htmlElementClasses[event]

            # Sending request to get all page information
            html = requests.get(website)
            # Converting it into a readable html page and stripping all un-necessary elements
            newContent = BeautifulSoup(html.text, 'html.parser').find(class_=classname).prettify()

            # Read current file content (we assume it always exists)
            with open('../data/' + event + '.html') as f:
                fileContent = f.read()

            if newContent == fileContent:
                print('There are no changes my friends!')
            else:
                # Write new HTML to the file
                with open('../data/' + event + '.html', 'w') as f:
                    f.write(newContent)

                notifier.notify(event)
                # Changing cell with last changed date
                if event in df.index:
                    df.at[event, 'Last change'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    df.loc[event] = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]

        # When the loop is over save all changes to csv
        df.to_csv('../data/changes.csv')


