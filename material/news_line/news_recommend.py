import pymysql
import json
from liff_api import *
# 載入基礎設定檔
secretFileContentJson=json.load(open("../line_secret_key",'r'))
server_url=secretFileContentJson.get("server_url")
'''

製作模板

'''
def recommend():
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news',
                           charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT url,title \
                       from test_news \
                       ORDER BY RAND() \
                       LIMIT 5"
                   )

    # 使用 fetchmany(n)方法获取n条数据.
    data = cursor.fetchmany(5)
    # print(data)
    # print(data[0][0])  # url
    # print(data[0][1])  # title
    conn.close()
    con = ""
    for i in data:
        title = i[1]
        url = i[0]
        bubble ="""
         {
                 "type": "bubble",
                 "body": {
                   "type": "box",
                   "layout": "vertical",
                   "spacing": "sm",
                   "contents": [
                     {
                       "type": "text",
                       "text": "%s",
                       "size": "xl",
                       "weight": "bold",
                       "wrap": true
                     }
                   ]
                 },
                 "footer": {
                   "type": "box",
                   "layout": "vertical",
                   "spacing": "sm",
                   "contents": [
                     {
                       "type": "button",
                       "action": {
                         "type": "uri",
                         "label": "內文點我",
                         "uri": "%s"
                       },
                       "color": "#52AC2F",
                       "style": "primary"
                     },
                     {
                       "type": "button",
                       "action": {
                         "type": "postback",
                         "label": "喜歡",
                         "data": "%s|like"
                       }
                     },
                     {
                       "type": "button",
                       "action": {
                         "type": "postback",
                         "label": "不喜歡",
                         "data": "%s|dislike"
                       }
                     }
                   ]
                 }
               },"""% (title, url, url, url)
        con += bubble

    flexCarouselContainerJsondict= """
    {
    "type": "carousel",
        "contents": ["""+con+"""
          {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "uri",
                    "label": "See more",
                    "uri": "https://www.google.com/"
                  },
                  "flex": 1,
                  "gravity": "center"
                }
              ]
            }
          }
        ]
      }
    """
    return flexCarouselContainerJsondict

# 國外新聞推薦模板
def foreign_recommend():
    #製作seemode的liff
    liff_init(secretFileContentJson.get("channel_access_token"))
    liffUrl = 'https://%s/recommend/seemode'%(str(server_url))
    liffID = (liff_add(liffUrl, "tall"))['liffId']
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news',
                           charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT news_title,news_link,img_link \
                       from hot_foreign_news \
                       ORDER BY RAND() \
                       LIMIT 5"
                   )

    # 使用 fetchmany(n)方法获取n条数据.
    data = cursor.fetchmany(5)
#     print(data)
#     print(data[0][0])  # title
#     print(data[0][1])  # url
#     print(data[0][2])  # img
    conn.close()
    con = ""

    for i in data:
        img = i[2]
        title = i[0]
        url = i[1]
        bubble = """
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "%s",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "text",
                        "text": "%s",
                        "size": "xl",
                        "weight": "bold",
                        "wrap": true
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "內文點我",
                            "uri": "%s"
                        },
                        "color": "#52AC2F",
                        "style": "primary"
                    }
                ]
            }
        },
        """ % (img, title, url)
        con += bubble


    foreign="""
    {
        "type": "carousel",
        "contents": [
            """+con+"""
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "See more",
                                "uri": "line://app/%s"
                            },
                            "flex": 1,
                            "gravity": "center"
                        }
                    ]
                }
            }
        ]
    }
    """%(str(liffID))
    return foreign