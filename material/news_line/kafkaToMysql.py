import pymysql
import json

def toMysql(msg):
    # 設定資料庫連線
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news',
                           charset='utf8')

    # 建立cursor
    cursor = conn.cursor()

    preference = json.loads(msg)
    replace_sql = "REPLACE INTO user_preference SET news_url='%s', userid='%s', preference='%s', timestamp='%d';" % \
                  (preference["news_url"], preference["userid"], preference["preference"], int(preference["timestamp"]))
    print(replace_sql)
    # 執行SQL
    try:
        cursor.execute(replace_sql)
        conn.commit()
        print("Successful!")
    except:
        conn.rollback()
        print("Failed!")

    # 關閉資料庫連線
    conn.close()
