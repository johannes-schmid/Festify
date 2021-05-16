import requests
# This is needed to search in the html response specific elements
from bs4 import BeautifulSoup
# Date time module to track stamp current time
import datetime
from google.cloud import datastore

datastore_client = datastore.Client()
# Creating Crawler Class
class Crawler:

    # Creating run call that crawls websites
    def run(self):

        events = datastore_client.query(kind='events').fetch()
        changedEvents = []
        for event in events:
            if 'website' not in event or 'elementClass' not in event or 'htmlContent' not in event:
                continue

            website = event['website']
            classname = event['elementClass']


            # Sending request to get all page information
            html = requests.get(website)
            if html.status_code != 200:
                continue
            # Converting it into a readable html page and stripping all un-necessary elements
            newContent = BeautifulSoup(html.text, 'html.parser').find(class_=classname).prettify()[:1499]

            # Read current file content (we assume it always exists)
            fileContent = event['htmlContent']

            if newContent == fileContent:
                print('There are no changes my friends!')
            else:
                # Write new HTML to the file
                event['htmlContent'] = newContent
                event['lastChange'] = datetime.datetime.now()
                datastore_client.put(event)

                changedEvents.append(event)
        return changedEvents

    def getEvents(self):

        events = datastore_client.query(kind='events').fetch()
        return list(events)