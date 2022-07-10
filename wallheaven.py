# https://wallhaven.cc/w/k7q9m7
# https://w.wallhaven.cc/full/k7/wallhaven-k7q9m7.png
# https://th.wallhaven.cc/lg/k7/k7q9m7.jpg

# https://wallhaven.cc/w/y8622k
# https://w.wallhaven.cc/full/y8/wallhaven-y8622k.jpg
# https://th.wallhaven.cc/lg/y8/y8622k.jpg

# https://wallhaven.cc/w/y86g17
# https://w.wallhaven.cc/full/y8/wallhaven-y86g17.jpg
# https://th.wallhaven.cc/lg/y8/y86g17.jpg

import json
from  requests.sessions import Session
import bs4
import requests

total = {}

with Session() as requests:
    headers = {
        'authority': 'wallhaven.cc',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'XSRF-TOKEN=eyJpdiI6IiszT1lrRkMzdFVGckQxR1NLU05pcGc9PSIsInZhbHVlIjoibUpjbGRPMW1PeEVrUkxyZUxEY3NndnlUNG9CS1Z0dUxqU1VnaFRTR1RJc1dMVkVBZ3B6YzFGSFRkN01vVjB1TiIsIm1hYyI6IjliNGZmNzlkM2NiMGY3MjYyNDY1YzkwZWMxYWZlOGY1NmJmMGVjZTY0MDU4YzkyOWI5YzNiZGM0ZWVlYmM5NWQifQ%3D%3D; wallhaven_session=eyJpdiI6Iml0TjVQWDRHSnNXbFdNK25VNENFNEE9PSIsInZhbHVlIjoiQjRweWJCS2JmVnU4aFpUd0JIdUdubVdNbHNCbXU1TTh4OGpCayt1SktGck9QeXJQY1F4MWFlUlRpeGp0aFJKcyIsIm1hYyI6IjcwNTQ4YWMwN2FhZWM4MDlhM2I1NjVjZDJiNzBkNjFmYjE0ZjQwZjE1NDBiYWNiNTRlYmJhMmRiOWNhYTU3NjMifQ%3D%3D',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://www.reddit.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.51',
    }

    full_link_template = 'https://w.wallhaven.cc/full/{}/wallhaven-{}.jpg'
    for i in range(1,270):
        params = (
            ('page', str(i)),
        )
        response = requests.get('https://wallhaven.cc/toplist', headers=headers, params=params)
        # response = requests.get('https://wallhaven.cc/', headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())
        links = soup.select(".lazyload")
        # print(links)
        tp = []
        for link in links:
            link = link.get('data-src')
            # print(link)
            temp = link.split('/')
            temp2 = full_link_template.format(temp[4],temp[-1].split(".")[0])
            # print(temp2)
            tp.append(temp2)
        if tp:
            total[i] = tp
with open('wallheaven.json', 'w') as f:
    json.dump(total, f)