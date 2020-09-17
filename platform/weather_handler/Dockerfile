FROM python:3

ADD / /

RUN /usr/local/bin/python -m pip install --upgrade pip &&\
    pip install requests && \
    pip install opcua && \
    pip install apscheduler

CMD [ "python","-u", "./weather.py" ]