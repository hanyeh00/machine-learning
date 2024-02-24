import requests
from bs4 import BeautifulSoup

login_url = 'http://example.com/login'
data = {
    'username': 'f9130268245',
    'password': '102030'
}
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'username': 'f9130268245',
    'password': '102030'
         }

# Post the payload to the site to log in
s = session.post("https://www.mahka.ir", data=payload)

# Navigate to the next page and scrape the data
s = session.get('https://mahka.ir/cs/UserMgmt/19/ورود-به-سایت')
print(s.text)
