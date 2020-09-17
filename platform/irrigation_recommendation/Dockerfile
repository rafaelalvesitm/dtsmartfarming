FROM python:3

ADD / /

RUN /usr/local/bin/python -m pip install --upgrade pip &&\
    pip install requests && \
    pip install apscheduler && \
    pip install pymysql && \
    pip install -U scikit-fuzzy && \
    python -m pip install -U matplotlib

CMD [ "python","-u", "./irrigation.py" ]