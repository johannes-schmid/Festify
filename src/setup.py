import datetime
import os
from google.cloud import datastore


datastore_client = datastore.Client()

users = [{
    'firstname': 'Robi',
    'lastname': 'Robman',
    'email': 'robi@robman.nl'
},
{
    'firstname': 'Hansi',
    'lastname': 'hansman',
    'email': 'hannes322@yahoo.de'
}
]
events = [{
    'name': 'Dekmantel',
    'website': 'https://www.dekmantelfestival.com/en/tickets/',
    'elementClass': 'tickets',
    'htmlContent': '',
    'lastChange': datetime.datetime.now(),
},
    {
    'name': 'Sonar',
    'website': 'https://sonar.es/es/2022/tickets',
    'elementClass': 'main-container sm-full-width page_tickets lg-margin-top',
    'htmlContent': '',
    'lastChange': datetime.datetime.now(),
    }

]

for user in users:

    entity = datastore.Entity(key=datastore_client.key('users'))
    entity.update({
        'firstname': user['firstname'],
        'lastname': user['lastname'],
        'email': user['email']
    })
    datastore_client.put(entity)

for event in events:

    entity = datastore.Entity(key=datastore_client.key('events'))
    entity.update({
            'name': event['name'],
            'website': event['website'],
            'elementClass': event['elementClass'],
            'htmlContent': event['htmlContent'],
            'lastChange': datetime.datetime.now(),
    })
    datastore_client.put(entity)

