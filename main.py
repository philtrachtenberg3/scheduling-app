from exchangelib import Credentials, Account, Configuration, DELEGATE

# Setup credentials for Exchange
credentials = Credentials('user@example.com', 'mypassword')

# If you know the server address and don't need autodiscovery
config = Configuration(server='mail.example.com', credentials=credentials)

# Setup account
account = Account(primary_smtp_address='user@example.com', config=config, autodiscover=False, access_type=DELEGATE)
