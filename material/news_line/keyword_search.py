def keyword():
    keyword="""
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
            "label": "關鍵字1",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "關鍵字2",
            "uri": "https://linecorp.com"
          }
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "flex": 1,
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "搜尋更多",
            "uri": "https://linecorp.com"
          }
        }
      ]
    }
  }
     """
    return keyword
