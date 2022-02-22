
"""  
Created on Tue Feb 22 18:03:00 2022

web scrap JPG files from a website

@author: Michael Getachew Tadesse

"""

import os
import requests 
from bs4 import BeautifulSoup 
import urllib.request 
from PIL import Image 


out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
            "Documents\\GLRSTA\\from_client\\SJRWMD\\usjrb_struc_photos"

os.chdir(out_dir)

# specify URL 
url = "https://secure.sjrwmd.com/docs/AGO_USJRB/Structures/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

image_tags = soup.find_all('a')

# print(image_tags)

links = []
for image_tag in image_tags:
    if image_tag['href'].endswith("JPG"):
        links.append(image_tag['href'])
    
# print(links)

# download photos
for struc in links:
    urllib.request.urlretrieve(
            "https://secure.sjrwmd.com/docs/AGO_USJRB/Structures/" + 
                                    struc, struc)