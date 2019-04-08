# 主程式
news_demo.py

# ngrok

    curl -s "localhost:4040/api/tunnels" | awk -F',' '{print $3}' | awk -F'"' '{print $4}' | awk -F'//' '{print $2}'
