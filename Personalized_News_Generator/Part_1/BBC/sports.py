import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta,date
import sys
import re




def get_data(url):
    try:
        # url = "https://www.bbc.com/sport/cricket"

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://www.bbc.com/sport/football",
            "Alt-Used": "www.bbc.com",
            "Connection": "keep-alive",
            "Cookie": "ckns_policy=111; _cb=BwmqLUC40Nk7KrgDq; _chartbeat2=.1725888502270.1726041332590.111.CatToYBqVaePHdhwfBN_G51DIgvRE.23; pa_privacy=%22optin%22; _pcid=%7B%22browserId%22%3A%227c6958be-4797-407c-96cd-352ed5211a49%22%2C%22_t%22%3A%22mgkr3njb%7Cm0wc667b%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIGYA2ABi644AmQQFYALDwDsYgIwiR3AJy0QAfXxkAtgHMA1jA5IAVgCMAPpp4B3AMb9JJkAF8gA; optimizelyEndUserId=oeu1725888503517r0.16370284371382116; dnsDisplayed=undefined; ccpaApplies=true; signedLspa=undefined; _sp_su=false; ckpf_ppid=3033e1adc491461e84c59a079487aa0c; ccpaUUID=c663b7ed-2ab3-450c-961c-2c44eab97650; permutive-id=00087531-cada-41c4-87e4-923c9b720b74; __gads=ID=e9ddbc88ca23dd4d:T=1725888546:RT=1726041374:S=ALNI_Mb_3UQYvXy-VoJ-tp9LnCUk5hxGqg; __gpi=UID=00000ef609f5ae63:T=1725888546:RT=1726041374:S=ALNI_MYM5oH5XU6iufcssqWcgljx1SWMbA; __eoi=ID=69196afc92a230ae:T=1725888546:RT=1726041374:S=AA-AfjYXPxxkV5fBkKots2y7EdEK; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHJldHVybjplN2Y1N2MxNTRhZWZmYWYxYjM0YWY2ZDZiYjcxMjg0ZjQ0NDUxMzllOjEiXX19LCJfdCI6Im1na3IzbmpifG0wd2M2NjdiIn0%3D; __pat=3600000; __pvi=eyJpZCI6InYtbTB4amllMWZxZjUycHQ3eiIsImRvbWFpbiI6Ii5iYmMuY29tIiwidGltZSI6MTcyNjAzOTc2NDYyN30%3D; xbc=%7Bkpex%7DNyr6e1kZttvU7eIR2ViCFg; cX_P=m0v1gbcw5uiezebc; ckns_mvt=502717b5-3622-4a7f-8975-aff3fc3f0fe5; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%227c6958be-4797-407c-96cd-352ed5211a49%22%2C%22options%22%3A%7B%22end%22%3A%222025-10-13T07%3A55%3A32.544Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _pbjs_userid_consent_data=3524755945110770; pa_vid=%227c6958be-4797-407c-96cd-352ed5211a49%22; _pcid=%7B%22browserId%22%3A%227c6958be-4797-407c-96cd-352ed5211a49%22%2C%22_t%22%3A%22mgkr3njb%7Cm0wc667b%22%7D; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHJldHVybjplN2Y1N2MxNTRhZWZmYWYxYjM0YWY2ZDZiYjcxMjg0ZjQ0NDUxMzllOjEiXX19LCJfdCI6Im1na3IzbmpifG0wd2M2NjdiIn0%3D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIGYA2ABi644AmQQFYALDwDsYgIwiR3AJy0QAfXxkAtgHMA1jA5IAVgCMAPpp4B3AMb9JJkAF8gA; _cb_svref=https%3A%2F%2Fwww.bbc.co.uk%2F; DM_SitId1778=1; DM_SitId1778SecId13934=1; ecos.dt=1726041339223; __tbc=%7Bkpex%7DVuf4q55GYzJ3U73ipEAplALBbUiZbLdlYecSSwuRmHTBjKJ-cKYAa9tdaJx01Hfb4KsDPkAcyg-anYlUere9oQ; DM_SitId1778SecId14803=1; _chartbeat5=151|125|%2Fsport%2Ffootball|https%3A%2F%2Fwww.bbc.com%2Fsport%2Fcricket|DBls33rUn2tCBCyIhCv6wimDS0ylO||c|Cw_drkMZTK7BNpoqHCh3C3NB1cbml|bbc.co.uk|",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Priority": "u=0, i",
            "TE": "trailers"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    except Exception as e:
        print("get_data func error ",e)


def main(source,output_file_name):
    try:

        sport_soup=get_data("https://www.bbc.com/sport")
        sport_list=sport_soup.find_all('li',class_="ssrcss-or45ca-StyledMenuItem eis6szr3")
        for i in sport_list:
            scraped_category=i.text
            url="https://www.bbc.com"+i.find('a')["href"]
            soup=get_data(url)
            news_list=soup.find_all('div',class_="ssrcss-tq7xfh-PromoContent exn3ah99")
            for i in news_list:
                try:
                    article_url="https://www.bbc.com"+i.find('a')["href"]
            
                except:
                    continue
                try:
                    news_raw=i.text.strip()
                except Exception as e:
                    # print(e)  
                    news_raw=""
                try:
                    title=i.find('a',class_="ssrcss-vdnb7q-PromoLink").text.strip()
            
                except Exception as e:
                    # print(e)
                    title=""
                try:
                    summary=news_raw.replace(title,"").strip()
                except Exception as e:
                    # print(e)
                    summary=""
                if title=="":
                    title=summary
                try:
                    published_time=i.find('span',class_="visually-hidden").text
                
                    if "ago" in published_time:
                        published_time=published_time.split("ago")[0].strip()
                        # print(published_time)
                        current_time = datetime.now()
                        if "hours" in published_time:
                            hours=int(published_time.split("hours")[0].strip())
                            published_date = current_time - timedelta(hours=hours)
                            
                            # print("time : ",formatted_time)           
                        elif "minutes" in published_time:
                            minutes= int(published_time.split("minutes")[0].strip())
                            published_date = current_time - timedelta(minutes=minutes)
                        elif "day" in published_time:
                            days=int(published_time.split("day")[0].strip())
                            published_date = current_time - timedelta(days=days)
                        else:
                            published_date=""
                    else:
                        try:
                            published_date = datetime.strptime(published_time, "%d %B %Y")
                        except:
                            try:
                                published_date = datetime.strptime(published_time, "%d %B").replace(year=2024)
                            except:
                                published_date=""
                    try:

                        published_date = published_date.strftime("%d-%m-%Y")
                    except:
                        published_date=""
                        continue
                except:
                    published_date=""
                    
                if published_date=="":
                    continue


                df_dict = {"Publication_date":published_date,"Source":source,"Scraped_category":scraped_category,
                           "Title":title,"Summary":summary,"news_raw":news_raw,"Article_Url":article_url
                       }
                print(df_dict)
                df = pd.DataFrame(df_dict, index=[0], columns=["Publication_date","Source","Scraped_category",
                           "Title","Summary","news_raw","Article_Url"
                                                            ])

                with open(output_file_name, 'a',encoding='utf-8',newline ='') as f:
                    df.to_csv(f, mode='a', header=f.tell()==0,index=False)

    except Exception as e:
        print("main func error : ",e)



if __name__ == "__main__":
    file_no = sys.argv[1]
    todays_date = str(date.today())
    todays_date = todays_date.replace("-", "_")
    source="BBC"
    output_file_name = f"BBC_sports_data_{todays_date}_{file_no}.csv"  
    main(source,output_file_name)