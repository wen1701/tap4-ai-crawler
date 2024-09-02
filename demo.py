import requests
import os 
import json
from  website_crawler import WebsitCrawler
import asyncio
website_crawler = WebsitCrawler()

source_list = open('./data/resource.json', 'r', encoding='utf-8').read()
source_list = json.loads(source_list)
web_info = []
for item in source_list:
    links = item.get("list")
    info = {}
    info["group_name"] = item.get("group_name")
    info['details'] = []
    for link in links:
        print(link.get("ori_url"))
        params = {
            "url": link.get("ori_url"),
            "tags": []
        }
        headers = {
            'authorization': 'Bearer 4487f197tap4ai8Zh42Ufi6mAHWGdy'
        }
        res = requests.post("http://127.0.0.1:8040/site/crawl",headers=headers, json=params)

        print(res.json())
        info['details'].append(res.json())
    
    web_info.append(info)

print(web_info)
with open('./data/web_info.json', 'w', encoding='utf-8') as f:
    json.dump(web_info, f, ensure_ascii=False, indent=4)
        