import datetime
import os
from google.cloud import datastore


# Cleaning Up Databases before creating them

datastore_client = datastore.Client()
query = datastore_client.query(kind='events')
all_keys = query.fetch()
datastore_client.delete_multi(all_keys)

datastore_client = datastore.Client()
query = datastore_client.query(kind='users')
all_keys = query.fetch()
datastore_client.delete_multi(all_keys)


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
    'name': 'hubi',
    'website': 'https://www.dekmantelfestival.com/en/tickets/',
    'htmlContent': '',
    'lastChange': datetime.datetime.now(),
    'imagefile': 'Dekmantel.png',
},
    {
    'name': 'Sonar',
    'website': 'https://sonar.es/es/2022/tickets',
    'htmlContent': '',
    'lastChange': datetime.datetime.now(),
    'imagefile': 'Sonar.png',
    }
,   {
    'name': 'Awakenings',
    'website': 'https://sonar.es/es/2022/tickets',
    'htmlContent': '',
    'lastChange': datetime.datetime.now(),
    'imagefile': 'Awakenings.png',
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
            'htmlContent': event['htmlContent'],
            'lastChange': datetime.datetime.now(),
            'imagefile': event['imagefile'],
    })
    datastore_client.put(entity)

