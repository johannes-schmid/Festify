from google.cloud import datastore

datastore_client = datastore.Client()


class SubscriptionManager:

    def getSubscribers(self):
        subscribers = datastore_client.query(kind='users').fetch()
        return list(subscribers)

    def subscribe(self, firstname, lastname, email):
        user = datastore.Entity(key=datastore_client.key('users'))
        user.update({
            'firstname': firstname,
            'lastname': lastname,
            'email': email
        })
        query = datastore_client.query(kind='users')
        existinguser = query.add_filter('email', '=', email).fetch(limit=1)

        if len(list(existinguser)) > 0:
            raise Exception('This user has already subscribed to this mailing list')

        datastore_client.put(user)

    def unsubscribe(self, mail):
        subscribers = datastore_client.query(kind='users')
        deleteuser = subscribers.add_filter('email', '=', mail).fetch(limit=1)
        user = list(deleteuser)[0]

        datastore_client.delete(user.key)
