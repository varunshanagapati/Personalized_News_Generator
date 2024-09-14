import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta,date
import sys
import re


def get_data(source,collection_id,output_file_name):

    j=0
    size=-1
    while size!=0:
        try:
            url = f"https://web-cdn.api.bbci.co.uk/xd/content-collection/{collection_id}"

            querystring = {
                "country":"in",
                "page":j,
                "size":"200"
                        }

            payload = ""
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Origin": "https://www.bbc.com",
                "Connection": "keep-alive",
                "Referer": "https://www.bbc.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Priority": "u=4"
            }

            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            data=response.json()

            size=len(data["data"])
            # print(size)
            for i in range(size):
                try:
                    article_url="https://www.bbc.com"+data["data"][i]["path"]
                except:
                    try:
                        article_url="https://www.bbc.com"+data["data"][i]["url"]
                    except:
                        article_url=""
                try:
                    scraped_category=data["data"][i]["subtype"]
                except:
                    scraped_category=""
                try:
                    title=data["data"][i]["title"]
                    title=re.sub(r'[^\x00-\x7F]+', ' ', title).strip()
                except:
                    title=""
                try:
                    summary=data["data"][i]["summary"]
                    summary=re.sub(r'[^\x00-\x7F]+', ' ', summary).strip()
                except:
                    summary=""
                try:
                    published_date=data["data"][i]["lastPublishedAt"].split("T")[0]
                except:
                    published_date=""
                try:
                    news_raw=str(data["data"][i])
                except:
                    news_raw=""

                df_dict = {"Publication_date":published_date,"Source":source,"Scraped_category":scraped_category,
                           "Title":title,"Summary":summary,"news_raw":news_raw,"Article_Url":article_url
                       }
                print(df_dict)
                df = pd.DataFrame(df_dict, index=[0], columns=["Publication_date","Source","Scraped_category",
                           "Title","Summary","news_raw","Article_Url"
                                                            ])

                with open(output_file_name, 'a',encoding='utf-8',newline ='') as f:
                    df.to_csv(f, mode='a', header=f.tell()==0,index=False)
            
            j+=1
        except Exception as e:
            print("get_data Func error",e)





def main(source_file_name,output_file_name):
    try:
        id_file=pd.read_csv(source_file_name)
        for row in id_file.iterrows():
            row=row[1]
            source=row["Source"]
            id=row["id"]


            get_data(source,id,output_file_name)


    except Exception as e:
        print("main func error : ",e)



if __name__ == "__main__":
    file_no = sys.argv[1]
    todays_date = str(date.today())
    todays_date = todays_date.replace("-", "_")
    source_file_name="news_ids.csv"
    output_file_name = f"BBC_data_{todays_date}_{file_no}.csv"  
    main(source_file_name,output_file_name)