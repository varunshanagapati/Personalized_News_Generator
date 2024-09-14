import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta
import sys
import json

def get_data(url):
    try:
        # url = "https://www.bbc.com/news/topics/c2vdnvdg6xxt"

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://www.bbc.com/news",
            "Alt-Used": "www.bbc.com",
            "Connection": "keep-alive",
            "Cookie": "ckns_policy=111; _cb=BwmqLUC40Nk7KrgDq; _chartbeat2=.1725888502270.1725967388561.11.DU0Tk68kaDw6oFGuB18gx9C7Cdb2.7; pa_privacy=%22optin%22; _pcid=%7B%22browserId%22%3A%227c6958be-4797-407c-96cd-352ed5211a49%22%2C%22_t%22%3A%22mgkr3njb%7Cm0wc667b%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIGYA2ABi644AmQQFYALDwDsYgIwiR3AJy0QAfXxkAtgHMA1jA5IAVgCMAPpp4B3AMb9JJkAF8gA; optimizelyEndUserId=oeu1725888503517r0.16370284371382116; dnsDisplayed=undefined; ccpaApplies=true; signedLspa=undefined; _sp_su=false; ckpf_ppid=3033e1adc491461e84c59a079487aa0c; ccpaUUID=c663b7ed-2ab3-450c-961c-2c44eab97650; permutive-id=00087531-cada-41c4-87e4-923c9b720b74; __gads=ID=e9ddbc88ca23dd4d:T=1725888546:RT=1725967351:S=ALNI_Mb_3UQYvXy-VoJ-tp9LnCUk5hxGqg; __gpi=UID=00000ef609f5ae63:T=1725888546:RT=1725967351:S=ALNI_MYM5oH5XU6iufcssqWcgljx1SWMbA; __eoi=ID=69196afc92a230ae:T=1725888546:RT=1725967351:S=AA-AfjYXPxxkV5fBkKots2y7EdEK; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHJldHVybjplN2Y1N2MxNTRhZWZmYWYxYjM0YWY2ZDZiYjcxMjg0ZjQ0NDUxMzllOjEiXX19LCJfdCI6Im1na3IzbmpifG0wd2M2NjdiIn0%3D; __pat=3600000; __pvi=eyJpZCI6InYtbTB3Ynl6NmNvMGtjOXU4aiIsImRvbWFpbiI6Ii5iYmMuY29tIiwidGltZSI6MTcyNTk2NzM4OTgwM30%3D; xbc=%7Bkpex%7DxOR5BC7TXdNUHV8ra5Lrdw; cX_P=m0v1gbcw5uiezebc; ckns_mvt=502717b5-3622-4a7f-8975-aff3fc3f0fe5; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%227c6958be-4797-407c-96cd-352ed5211a49%22%2C%22options%22%3A%7B%22end%22%3A%222025-10-12T10%3A15%3A25.361Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _pbjs_userid_consent_data=3524755945110770; pa_vid=%227c6958be-4797-407c-96cd-352ed5211a49%22; _pcid=%7B%22browserId%22%3A%227c6958be-4797-407c-96cd-352ed5211a49%22%2C%22_t%22%3A%22mgkr3njb%7Cm0wc667b%22%7D; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHJldHVybjplN2Y1N2MxNTRhZWZmYWYxYjM0YWY2ZDZiYjcxMjg0ZjQ0NDUxMzllOjEiXX19LCJfdCI6Im1na3IzbmpifG0wd2M2NjdiIn0%3D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIGYA2ABi644AmQQFYALDwDsYgIwiR3AJy0QAfXxkAtgHMA1jA5IAVgCMAPpp4B3AMb9JJkAF8gA; DM_SitId1778=1; DM_SitId1778SecId13934=1; ecos.dt=1725968145275; DM_SitId1778SecId14803=1; _cb_svref=external; lux_uid=172596737648991654; __tbc=%7Bkpex%7DVuf4q55GYzJ3U73ipEAplALBbUiZbLdlYecSSwuRmHTBjKJ-cKYAa9tdaJx01Hfb4KsDPkAcyg-anYlUere9oQ",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0, i"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except Exception as e:
        print("get func error : ",e)

def main(source,output_file_name):
    try:
        cat=get_data("https://www.bbc.com")
        cat_list=cat.find_all('li',class_="sc-f116bf72-3")
        for i in cat_list:
            category_url="https://www.bbc.com"+i.find('a')["href"]

            news=get_data(category_url)
            
            news_list=news.find_all('li',class_="sc-f116bf72-5 bnxbUg")
            for i in news_list:
                try:
                    scraped_category=i.find('a').text
                except:
                    scraped_category=""
                try:
                    url="https://www.bbc.com"+i.find('a')["href"]
                except:
                    url=""
                try:
                    soup=get_data(url)

                    id_l=soup.find('script', id='__NEXT_DATA__').text
                    data= json.loads(id_l)
                    try:
                        collection_id=data["props"]["pageProps"]["page"][next(iter(data["props"]["pageProps"]["page"]))]["sections"][-1]["collectionId"]
                    except:
                        collection_id=data["props"]["pageProps"]["page"][next(iter(data["props"]["pageProps"]["page"]))]["sections"][-2]["collectionId"]
                except:
                    collection_id=""

                
                df_dict = {"Source":source,"Scraped_category":scraped_category,"id":collection_id,"Url":url
                        }
                print(df_dict)
                df = pd.DataFrame(df_dict, index=[0], columns=["Source","Scraped_category","id","Url"
                                                            ])

                with open(output_file_name, 'a',encoding='utf-8',newline ='') as f:
                    df.to_csv(f, mode='a', header=f.tell()==0,index=False)
    except Exception as e:
        print("Main func error: ",e)


if __name__ == "__main__":
    output_file_name = "news_ids.csv"  
    source="BBC"
    main(source,output_file_name)