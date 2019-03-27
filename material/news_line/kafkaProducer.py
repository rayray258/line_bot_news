from kafka import KafkaProducer
import json, sys

def toKafka(topic, key, msg):
    # 步驟1.設定要連線到Kafka集群的相關設定, 並產生一個Kafka的Producer的實例
    producer = KafkaProducer(
        # Kafka集群在哪裡?
        bootstrap_servers=["34.80.48.32:9092"],
        api_version = (0, 10),
        # 指定msgKey的序列化器, 若Key為None, 無法序列化, 透過producer直接給值
        key_serializer=str.encode,
        # 指定msgValue的序列化器
        value_serializer=str.encode
    )

    # 步驟2.指定想要發佈訊息的topic名稱
    topic_name = topic

#     msg = json.dumps(msg)

    msg_counter = 0
    try:
        print("Start sending messages ...")
        # 步驟3.產生要發佈到Kafka的訊息
        # - 參數  # 1: topicName
        # - 參數  # 2: msgKey
        # - 參數  # 3: msgValue
        producer.send(topic=topic_name, key=key, value=msg)
        msg_counter += 1
        print("Send " + str(msg_counter) + " messages to Kafka")
        print("Message sending completed!")
        producer.flush()
    except Exception as e:
        # 錯誤處理
        e_type, e_value, e_traceback = sys.exc_info()
        print("type ==> %s" % (e_type))
        print("value ==> %s" % (e_value))
        print("traceback ==> file name: %s" % (e_traceback.tb_frame.f_code.co_filename))
        print("traceback ==> line no: %s" % (e_traceback.tb_lineno))
        print("traceback ==> function name: %s" % (e_traceback.tb_frame.f_code.co_name))
    finally:
        # 步驟4.關掉Producer實例的連線
        producer.close()