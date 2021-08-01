import requests
# This is needed to search in the html response specific elements
from bs4 import BeautifulSoup
# Date time module to track stamp current time
import datetime
from google.cloud import datastore

from .Notifier import Notifier

datastore_client = datastore.Client()


# Creating Crawler Class
class Crawler:

    def run(self):

        events = datastore_client.query(kind='events').fetch()
        notifier = Notifier()
        for event in events:
            if 'website' not in event or 'htmlContent' not in event:
                continue

            website = event['website']

            # Sending request to get all page information
            html = requests.get(website)
            if html.status_code != 200:
                continue
            # Converting it into a readable html page and stripping all un-necessary elements

            htmlContent = BeautifulSoup(html.content, 'html.parser')
            newContent = ' '.join(htmlContent.find_all(text=True))[:1499]

            # Read current file content (we assume it always exists)
            fileContent = event['htmlContent']

            if newContent != fileContent:
                # Write new HTML to the file
                event['htmlContent'] = newContent
                event['lastChange'] = datetime.datetime.now()
                datastore_client.put(event)
                notifier.notify(event)

    def getEvents(self):

        events = datastore_client.query(kind='events').fetch()
        return list(events)
