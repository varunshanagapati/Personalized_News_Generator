import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta,date
import sys
import re




def get_data(url):
    try:
        # url = "https://news.sky.com/politics"

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://news.sky.com/uk",
            "Connection": "keep-alive",
            "Cookie": "testGroup=B; uuid=aac128561baca38517e7b885d60081bc; _sp_su=false; adobeujs-optin=%7B%22aam%22%3Afalse%2C%22adcloud%22%3Afalse%2C%22aa%22%3Afalse%2C%22campaign%22%3Afalse%2C%22ecid%22%3Afalse%2C%22livefyre%22%3Afalse%2C%22target%22%3Afalse%2C%22mediaaa%22%3Afalse%7D; euconsent-v2=CQEyKcAQEyKcAAGABBENBGFgAAAAAEPgABBoAAAOWgJAAkABkAEcARwAnAByADnAIAAQcAjgBdQFSgLUAXQAvMBggDFgHLABBQAIC6CgAEAjgAAA.YAAAAAAAAAAA; consentUUID=6d2fe431-277e-4d89-9f33-e951fd3cfde6_35; consents=::",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
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

        cat_soup=get_data("https://news.sky.com")
        cat_list=cat_soup.find('div',class_="ui-news-header-nav-items-wrap").find_all('a')
        for i in range(1,len(cat_list)):
            try:
                scraped_category=cat_list[i].text.strip()
            except:
                scraped_category=""
            try:
                url="https://news.sky.com"+cat_list[i]["href"]

                soup=get_data(url)
                try:
                    news_list=soup.find_all('div',class_="ui-story-body")

                    for j in news_list:
                        try:
                            title=j.find_all('a')[-1].text.strip()
                        except:
                            title=""
                        try:
                            article_url="https://news.sky.com"+j.find_all('a')[-1]["href"]
                        except:
                            article_url=""
                        try:
                            news_raw=j.text.strip()
                        except:
                            news_raw=""

                        df_dict = {"Source":source,"Scraped_category":scraped_category,
                           "Title":title,"news_raw":news_raw,"Article_Url":article_url
                            }
                        print(df_dict)
                        df = pd.DataFrame(df_dict, index=[0], columns=["Source","Scraped_category",
                           "Title","news_raw","Article_Url"
                                                                    ])

                        with open(output_file_name, 'a',encoding='utf-8',newline ='') as f:
                            df.to_csv(f, mode='a', header=f.tell()==0,index=False)


                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)




    except Exception as e:
        print("main func error : ",e)



if __name__ == "__main__":
    file_no = sys.argv[1]
    todays_date = str(date.today())
    todays_date = todays_date.replace("-", "_")
    source="SkyNews"
    output_file_name = f"SkyNews_L1_data_{todays_date}_{file_no}.csv"  
    main(source,output_file_name)