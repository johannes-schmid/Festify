import pandas as pd


class SubscriptionManager:

    def getSubscribers(self):
        subscribers = pd.read_csv('../../data/users.csv')
        return subscribers

    def subscribe(self,firstname, lastname, email):
        subscribers = pd.read_csv('../../data/users.csv', index_col=False)
        newSubscriber = {'firstname':firstname,'lastname': lastname, 'e-mail': email}
        subscribers.append(newSubscriber, ignore_index=True, sort=True)
        subscribers.to_csv('../../data/users.csv')

    def unsubscribe(self,mail):
        subscribers = pd.read_csv('../../data/users.csv', index_col='e-mail')
        subscribers.drop(index=mail, inplace=True)
        subscribers.to_csv('../../data/users.csv')

