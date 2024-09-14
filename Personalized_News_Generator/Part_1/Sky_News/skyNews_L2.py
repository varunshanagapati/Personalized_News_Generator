import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta,date
import sys
import re


def get_data(source,scraped_category,article_url,output_file_name):
    try:
        # url = "https://news.sky.com/story/uk-economy-continued-to-flatline-in-month-labour-came-to-power-official-figures-13212719"

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Connection": "keep-alive",
            "Cookie": "testGroup=B; uuid=aac128561baca38517e7b885d60081bc; _sp_su=false; adobeujs-optin=%7B%22aam%22%3Afalse%2C%22adcloud%22%3Afalse%2C%22aa%22%3Afalse%2C%22campaign%22%3Afalse%2C%22ecid%22%3Afalse%2C%22livefyre%22%3Afalse%2C%22target%22%3Afalse%2C%22mediaaa%22%3Afalse%7D; euconsent-v2=CQEyKcAQEyKcAAGABBENBGFgAAAAAEPgABBoAAAOWgJAAkABkAEcARwAnAByADnAIAAQcAjgBdQFSgLUAXQAvMBggDFgHLABBQAIC6CgAEAjgAAA.YAAAAAAAAAAA; consentUUID=6d2fe431-277e-4d89-9f33-e951fd3cfde6_35; consents=::",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Priority": "u=0, i",
            "TE": "trailers"
        }

        response = requests.request("GET", article_url, data=payload, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            title=soup.find('h1',class_="sdc-article-header__title").text
        except:
            title=""
        try:
            summary=""
            para_list=soup.find('div',class_="sdc-article-body sdc-article-body--story sdc-article-body--lead").find_all('p')
            for i in para_list:
                try:
                    summary+=i.text.strip()
                except:
                    pass
        except:
            try:
                summary=""
                para_list=soup.find('div',class_="sdc-article-header__titles").find_all('p')
                for i in para_list:
                    try:
                        summary+=i.text.strip()
                    except:
                        pass
            except:
                summary=""
            
            
        try:
            published_date=" ".join(soup.find('p',class_="sdc-article-date__date-time").text.split()[1:4])
            published_date = datetime.strptime(published_date, "%d %B %Y").strftime("%d-%m-%Y")
        except:
            published_date=""


        df_dict = {"Publication_date":published_date,"Source":source,"Scraped_category":scraped_category,
                    "Title":title,"Summary":summary,"Article_Url":article_url
                }
        print(df_dict)
        df = pd.DataFrame(df_dict, index=[0], columns=["Publication_date","Source","Scraped_category",
                    "Title","Summary","Article_Url"
                                                    ])

        with open(output_file_name, 'a',encoding='utf-8',newline ='') as f:
            df.to_csv(f, mode='a', header=f.tell()==0,index=False)


    except Exception as e:
        print("get_data func error: ",e)



def main(start_count,end_count,source_file,output_file_name):
    try:
        url_file=pd.read_csv(source_file)
        for row in url_file[start_count:end_count].iterrows():
            row=row[1]
            source=row["Source"]
            scraped_category=row["Scraped_category"]
            article_url=row["Article_Url"]
            get_data(source,scraped_category,article_url,output_file_name)

    except Exception as e:
        print(e)




if __name__ == "__main__":
    file_no = sys.argv[1]
    start_count = int(sys.argv[2])
    end_count = int(sys.argv[3])
    todays_date = str(date.today())
    todays_date = todays_date.replace("-", "_")
    source_file="SkyNews_L1_data_2024_09_11.csv"
    output_file_name = f"SkyNews_data_{todays_date}_{file_no}.csv"  
    main(start_count,end_count,source_file,output_file_name)