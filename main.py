from pprint import pprint
from requests import Session
import bs4
import re

with Session() as requests:
    headers = {
        'authority': 'interfacelift.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'PHPSESSID=0fdfd0cc794e91ace4a4e6d06203a8a9',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://interfacelift.com/wallpaper/downloads/date/any/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.51',
    }
    page_wise_links = {
        
    }
    try:
        for i in range(1,388):

            response = requests.get(f'https://interfacelift.com/wallpaper/downloads/downloads/any/index{i}.html', headers=headers)
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            selects = soup.select('select')
            on_changes:list[str] = [select.get('onchange') for select in selects]
            image_link_template = 'https://interfacelift.com/wallpaper/7yz4ma1/{}_{}_2560x1440.jpg'
            links=[]
            for on_change in on_changes:
                base,idp = re.search(r"\'([a-z0-9]+)\', this,\'(\d+)\'", on_change).groups()
                idp = str(idp)
                if len(idp) < 5:
                    idp = (5-len(idp) )* '0' +idp 
                links.append(image_link_template.format(idp,base))
            page_wise_links[i] = links   
    except Exception as e:
        print(e)


        
import json
with open('page_wise_links2.json', 'w') as f:
    json.dump(page_wise_links, f)
