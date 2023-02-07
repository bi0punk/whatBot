from datetime import time, date
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup 
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import pandas as pd
import threading
import pywhatkit
import requests
import datetime
import emoji
import csv
import re




r  = requests.get("http://www.game-debate.com/games/index.php?g_id=21580&game=000%20Plus").content
soup = BeautifulSoup(r,"lxml")
cont = soup.select("div.systemRequirementsRamContent")
ram = cont.select("span")
print(ram)
print(ram["title"], ram.text)
for span in soup.select("div.systemRequirementsSmallerBox.sysReqGameSmallBox span"):
    print(span["title"],span.text)


