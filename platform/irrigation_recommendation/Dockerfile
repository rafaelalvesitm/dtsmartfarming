FROM python:3.10

ADD . .

RUN pip install requests && \
    pip install apscheduler && \
    pip install pymysql && \
    pip install scikit-fuzzy && \
    pip install matplotlib

CMD [ "python","-u", "./irrigation.py" ]