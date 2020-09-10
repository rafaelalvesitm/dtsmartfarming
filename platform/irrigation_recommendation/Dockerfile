FROM python:3

ADD / /

RUN pip install requests && \
    pip install apscheduler && \
    pip install pymysql 

CMD [ "python","-u", "./irrigation.py" ]