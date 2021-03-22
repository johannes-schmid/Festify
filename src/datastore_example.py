from google.cloud import datastore
import os

os.environ["DATASTORE_DATASET"] = "test"
os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8534"
os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8534/datastore"
os.environ["DATASTORE_HOST"] = "http://localhost:8534"
os.environ["DATASTORE_PROJECT_ID"] = "test"

datastore_client = datastore.Client()

def store_user(userName):
    user = datastore.Entity(key=datastore_client.key('user'))
    user.update({
        'name': userName,
    })

    datastore_client.put(user)


def fetch_users():
    query = datastore_client.query(kind='user')
    query.order = ['name']

    users = query.fetch()

    return users


# example usage
userName = 'hansipansi'
store_user(userName)

allUsers = fetch_users()
for dbUser in allUsers:
    print("User: " + dbUser['name'])
