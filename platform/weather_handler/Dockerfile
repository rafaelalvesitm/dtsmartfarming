FROM python:3

ADD / /

RUN pip install requests && \
pip install opcua && \
pip install apscheduler

CMD [ "python","-u", "./weather.py" ]