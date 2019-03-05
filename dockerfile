FROM jupyter/base-notebook
RUN pip install Flask==0.12 requests line-bot-sdk
RUN pip install redis
RUN pip install PyMySQL
RUN pip install python-logstash
RUN pip install qrcode
RUN pip install image
RUN pip install python-dotenv
RUN pip install kafka-python
RUN pip install pykafka

#USER root
#RUN apt-get -y update
#RUN apt-get -y dist-upgrade
#RUN apt -y install mysql-server-5.7
#RUN apt -y install mysql-community-server
#RUN apt -y install python-dev default-libmysqlclient-dev
#RUN apt -y install python3-dev

#USER jovyan
#RUN pip install mysqlclient
